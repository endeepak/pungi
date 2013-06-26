from .expectations import Expectation
from .spy import Method, Object
from .matchers import Base as MatcherBase, add
from .any import Any


def expect(actual, *args, **kwargs):
    return Expectation(actual, *args, **kwargs)


def spyOn(target, methodName, **kwargs):
    originalMethod = getattr(target, methodName, None)
    return Method.create(target, methodName, originalMethod, **kwargs)


def createSpy(name=None, **methodsWithReturnValue):
    return Object.create(name, **methodsWithReturnValue)


def stopSpying():
    Method.stop()


def any(clazz):
    return Any(clazz)


add(*MatcherBase.__subclasses__())
