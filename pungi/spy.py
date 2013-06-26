import inspect


_CALL_NUMBER = 1


class Method(object):
    _all = []

    @classmethod
    def create(cls, target, methodName, originalMethod=None, **kwargs):
        spy = cls(target, methodName, originalMethod, **kwargs)
        setattr(target, methodName, spy)
        cls._track(spy)
        return spy

    @classmethod
    def _track(cls, spy):
        cls._all.append(spy)

    @classmethod
    def stop(cls):
        global _CALL_NUMBER
        for spy in cls._all:
            spy._rollback()
        del cls._all[:]
        _CALL_NUMBER = 1

    def __init__(self, target, methodName, originalMethod, returnValue=None,
                 raiseException=None, callThrough=False, callFake=None):
        self._target = target
        self._methodName = methodName
        self._originalMethod = originalMethod
        self._calls = []
        self.returnValue = returnValue or Object(methodName)
        self.raiseException = raiseException
        self.callThrough = callThrough
        self.callFake = callFake

    def __call__(self, *args, **kwargs):
        self._record_call(args, kwargs)
        if(self.callThrough):
            return self._originalMethod(*args, **kwargs)
        if(self.callFake):
            argspec = inspect.getargspec(self.callFake)
            if(len(argspec[0]) > 1 or
                    not inspect.ismethod(self.callFake) and argspec[0] or
                    argspec[1] is not None or
                    argspec[2] is not None):
                return self.callFake(*args, **kwargs)
            return self.callFake()
        if(self.raiseException is not None):
            raise self.raiseException
        return self.returnValue

    def _record_call(self, args, kwargs):
        global _CALL_NUMBER
        self._calls.append(Call(args, kwargs, _CALL_NUMBER))
        _CALL_NUMBER += 1

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        self._rollback()

    def __repr__(self):
        return "{0}.{1}".format(repr(self._target), self._methodName)

    @property
    def callCount(self):
        return len(self._calls)

    def wasCalled(self, times=None):
        if(times is not None):
            return self.callCount == times
        return self.callCount > 0

    def wasCalledBefore(self, method):
        return self.callNumber < method.callNumber

    def wasCalledWith(self, *args, **kwargs):
        for call in self._calls:
            if(call.received(*args, **kwargs)):
                return True
        return False

    @property
    def mostRecentCall(self):
        return self._calls[-1]

    def argsForCall(self, callIndex):
        return self._calls[callIndex].args

    def kwargsForCall(self, callIndex):
        return self._calls[callIndex].kwargs

    @property
    def callNumber(self):
        return self.mostRecentCall.number

    def andReturn(self, returnValue):
        self.returnValue = returnValue
        return self

    def andRaise(self, excpetion):
        self.raiseException = excpetion
        return self

    def andCallThrough(self):
        self.callThrough = True
        return self

    def andCallFake(self, fakeMethod):
        self.callFake = fakeMethod
        return self

    def _rollback(self):
        setattr(self._target, self._methodName, self._originalMethod)


class Call(object):

    def __init__(self, args, kwargs, number):
        self.args = args
        self.kwargs = kwargs
        self.number = number

    def received(self, *args, **kwargs):
        return (self.args, self.kwargs) == (args, kwargs)


class Object(object):

    @classmethod
    def create(cls, name, **methodsWithReturnValue):
        obj = cls(name)
        for method, returnValue in methodsWithReturnValue.items():
            Method.create(obj, method, returnValue=returnValue)
        return obj

    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr_name):
        return Method.create(self, attr_name)

    def __str__(self):
        return "<spy name={0}>".format(self.name)
