class Spy(object):

    @staticmethod
    def create(target, methodName, **kwargs):
        originalMethod = getattr(target, methodName)
        spy = Spy(target, methodName, originalMethod, **kwargs)
        setattr(target, methodName, spy)
        return spy

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

    def __call__(self, *args):
        self._calls.append(Call(args))
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

    def callCount(self):
        return len(self._calls)

    def wasCalled(self):
        return self.callCount() > 0

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

    def __init__(self, args):
        self.args = args
