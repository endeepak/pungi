import re
import sys
from .string import humanize, pp
from .expectations import Expectation


def add(*matchers):
    for matcher in matchers:
        Expectation.addMatcher(matcher)


class Base(object):

    def __init__(self, actual, *expectedArgs, **expectedKwArgs):
        self.actual = actual
        self.expectedArgs = expectedArgs
        self.expectedKwArgs = expectedKwArgs
        self.negated = NegativeMatcher(self)

    def matchesExpectation(self):
        return self.matches(*self.expectedArgs, **self.expectedKwArgs)

    def message(self):
        ''' Override this to provide failure message'''
        name = self.__class__.__name__
        return "{0} {1}".format(humanize(name),
                        pp(*self.expectedArgs, **self.expectedKwArgs))

    def matches(self):
        ''' Override this to verify assert'''
        pass


class NegativeMatcher(object):

    def __init__(self, assertion):
        self.assertion = assertion

    def matchesExpectation(self):
        return not self.assertion.matchesExpectation()

    def message(self):
        return "not {0}".format(self.assertion.message())


class ToBe(Base):

    def matches(self, expected):
        return self.actual == expected


class ToEqual(Base):

    def matches(self, expected):
        return self.actual == expected


class ToBeNone(Base):

    def matches(self):
        return self.actual is None


class ToBeTruthy(Base):

    def matches(self):
        return self.actual is True


class ToBeFalsy(Base):

    def matches(self):
        return self.actual is False


class ToMatch(Base):

    def matches(self, expected):
        return re.match(expected, self.actual)


class ToContain(Base):

    def matches(self, expected):
        return expected in self.actual


class ToBeGreaterThan(Base):

    def matches(self, expected):
        return self.actual > expected


class ToBeLessThan(Base):

    def matches(self, expected):
        return self.actual < expected


class ToRaise(Base):

    def matches(self, expectedException, message=None):
        try:
            self.actual()
        except:
            ex_type, ex = sys.exc_info()[:2]
            if(issubclass(ex_type, expectedException) and
                    (message is None or ex.args[0] == message)):
                return True


class ToHaveBeenCalled(Base):

    def matches(self, times=None):
        return self.actual.wasCalled(times=times)


class ToHaveBeenCalledWith(Base):

    def matches(self, *args, **kwargs):
        return self.actual.wasCalledWith(*args, **kwargs)


class ToHaveBeenCalledBefore(Base):

    def matches(self, method):
        return self.actual.wasCalledBefore(method)
