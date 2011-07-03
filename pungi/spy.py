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
        for spy in cls._all:
            spy._rollback()
        del cls._all[:]

    def __init__(self, target, methodName, originalMethod, returnValue=None,
                raiseException=None, callThrough=False, callFake=None):
        self._target = target
        self._methodName = methodName
        self._originalMethod = originalMethod
        self._returnValue = returnValue
        self._calls = []
        self._raiseException = raiseException
        self._callThrough = callThrough
        self._callFake = callFake

    def __call__(self, *args, **kwargs):
        self._calls.append(Call(args, kwargs))
        if(self._callThrough):
            return self._originalMethod()
        if(self._callFake):
            return self._callFake()
        if(self._raiseException is not None):
            raise self._raiseException
        return self._returnValue

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        self._rollback()

    @property
    def callCount(self):
        return len(self._calls)

    def wasCalled(self, times=None):
        if(times is not None):
            return self.callCount == times
        return self.callCount > 0

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

    def andReturn(self, returnValue):
        self._returnValue = returnValue
        return self

    def andRaise(self, excpetion):
        self._raiseException = excpetion
        return self

    def andCallThrough(self):
        self._callThrough = True
        return self

    def andCallFake(self, fakeMethod):
        self._callFake = fakeMethod
        return self

    def _rollback(self):
        setattr(self._target, self._methodName, self._originalMethod)


class Call(object):

    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

    def received(self, *args, **kwargs):
        return (self.args, self.kwargs) == (args, kwargs)

class Object(object):

    @classmethod
    def create(cls, name, **methodsWithReturnValue):
        obj = cls(name)
        for method, returnValue in methodsWithReturnValue.iteritems():
            Method.create(obj, method, returnValue=returnValue)
        return obj

    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr_name):
        return Method.create(self, attr_name)
