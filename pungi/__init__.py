import unittest
from expectations import Expectation
from spy import Spy


def expect(actual):
    return Expectation(actual)


def spyOn(target, method, returnValue=None):
    return Spy.create(target, method, returnValue)
