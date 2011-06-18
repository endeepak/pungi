from pungi import string


class Base(object):

    def __init__(self, actual, *expectedValues):
        self.actual = actual
        self.expectedValues = expectedValues
        self.negated = NegativeMatcher(self)

    def message(self):
        ''' Override this to provide failure message'''
        name = self.__class__.__name__
        return "{0} {1}".format(string.humanize(name),
                            string.pp(*self.expectedValues))

    def matches(self):
        ''' Override this to verify assert'''
        pass


class NegativeMatcher(Base):

    def __init__(self, assertion):
        self.assertion = assertion

    def matches(self):
        return not self.assertion.matches()

    def message(self):
        return "not {0}".format(self.assertion.message())


class ToBe(Base):

    def matches(self):
        return self.actual == self.expectedValues[0]


class ToHaveBeenCalled(Base):

    def matches(self):
        return self.actual.wasCalled()
