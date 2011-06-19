import unittest
from expectations import Expectation


def expect(actual):
    return Expectation(actual)


def spyOn(target, methodName, **kwargs):
    return spy.Method.create(target, methodName, **kwargs)
