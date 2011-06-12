class Expectation(object):

    def __init__(self, actual):
        self.actual = actual

    def toBe(self, *expectedValues):
        ToBeAssertion(self.actual, *expectedValues).verify()

    def notToBe(self, *expectedValues):
        ToBeAssertion(self.actual, *expectedValues).negated.verify()

    def toHaveBeenCalled(self, *expectedValues):
        ToHaveBeenCalledAssertion(self.actual, *expectedValues).verify()


class Assertion(object):

    def __init__(self, actual, *expectedValues):
        self.actual = actual
        self.expectedValues = expectedValues
        self.negated = NegativeAssertion(self)

    def verify(self):
        if(self.fails()):
            raise AssertionError(self.failure_message())

    def fails(self):
        return not self.passes()

    def negative_failure_message(self):
        ''' Override this to provide negative failure message'''
        return "Not {0}".format(self.failure_message())

    def failure_message(self):
        ''' Override this to provide failure message'''
        pass

    def passes(self):
        ''' Override this to verify assert'''
        pass


class NegativeAssertion(Assertion):

    def __init__(self, assertion):
        self.assertion = assertion

    def passes(self):
        return self.assertion.fails()

    def failure_message(self):
        return self.assertion.negative_failure_message()


class ToBeAssertion(Assertion):

    def expected(self):
        return self.expectedValues[0]

    def passes(self):
        return self.actual == self.expected()

    def failure_message(self):
        return "Expected {0} to equal {1}".format(
                        repr(self.actual), repr(self.expected()))

    def negative_failure_message(self):
        return "Expected {0} not to equal {1}".format(
                        repr(self.actual), repr(self.expected()))


class ToHaveBeenCalledAssertion(Assertion):

    def passes(self):
        return self.actual.wasCalled()

    def failure_message(self):
        return "Expected {0} to have been called".format(repr(self.actual))

    def negative_failure_message(self):
        return "Expected {0} not to have been called".format(repr(self.actual))
