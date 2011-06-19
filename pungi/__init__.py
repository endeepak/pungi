import unittest
from expectations import Expectation
from pungi import spy


def expect(actual):
    return Expectation(actual)


def spyOn(target, methodName, **kwargs):
    originalMethod = getattr(target, methodName)
    return spy.Method.create(target, methodName, originalMethod, **kwargs)


def createSpy(name=None, **methodsWithReturnValue):
    return spy.Object.create(name, **methodsWithReturnValue)


def stopSpying():
    spy.Method.stop()