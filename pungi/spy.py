class Spy(object):

    @staticmethod
    def create(target, methodName, returnValue):
        originalMethod = getattr(target, methodName)
        spy = Spy(target, methodName, originalMethod, returnValue)
        setattr(target, methodName, spy)
        return spy

    def __init__(self, target, methodName, originalMethod, returnValue=None):
        self.target = target
        self.methodName = methodName
        self.originalMethod = originalMethod
        self.returnValue = returnValue
        self.calls = []

    def __call__(self, *args):
        self.calls.append(Call(args))
        return self.returnValue

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        self.rollback()

    def callCount(self):
        return len(self.calls)

    def wasCalled(self):
        return self.callCount() > 0

    def andReturn(self, returnValue):
        self.returnValue = returnValue
        return self

    def rollback(self):
        setattr(self.target, self.methodName, self.originalMethod)


class Call(object):

    def __init__(self, args):
        self.args = args
