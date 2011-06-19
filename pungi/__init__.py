import unittest
from expectations import Expectation
from pungi import spy


def expect(actual):
    return Expectation(actual)


def spyOn(target, methodName, **kwargs):
    originalMethod = getattr(target, methodName)
    return spy.Method.create(target, methodName, originalMethod,**kwargs)


def createSpy(name=None):
    return spy.Object(name)