import unittest
from expectations import Expectation
from pungi import spy


def expect(actual, *args, **kwargs):
    return Expectation(actual, *args, **kwargs)


def spyOn(target, methodName, **kwargs):
    originalMethod = getattr(target, methodName, None)
    return spy.Method.create(target, methodName, originalMethod, **kwargs)


def createSpy(name=None, **methodsWithReturnValue):
    return spy.Object.create(name, **methodsWithReturnValue)


def stopSpying():
    spy.Method.stop()
