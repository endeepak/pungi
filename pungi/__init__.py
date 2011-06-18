import unittest
from expectations import Expectation
from spy import Spy


def expect(actual):
    return Expectation(actual)


def spyOn(target, methodName, **kwargs):
    return Spy.create(target, methodName, **kwargs)
