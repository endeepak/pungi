import unittest
from expectations import Expectation
from spy import Spy


def expect(actual):
    return Expectation(actual)


def spyOn(*args, **kwargs):
    return Spy.create(*args, **kwargs)
