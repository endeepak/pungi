import matchers
import types


class Expectation(object):

    def __init__(self, actual):
        self.actual = actual

    def verify(self, matcher):
        if(not matcher.matchesExpectation()):
            self.fail("Expected {0} {1}".format(
                        repr(self.actual), matcher.message()))

    def fail(slef, message):
        raise AssertionError(message)

    @classmethod
    def addMatcher(cls, matcherClass):
        matcher_name = matcherClass.__name__
        method_name = matcher_name[0].lower() + matcher_name[1:]
        negated_method_name = "not" + matcher_name

        def matcher_function(self, *expectedValues):
            self.verify(matcherClass(self.actual, *expectedValues))

        def negated_matcher_function(self, *expectedValues):
            self.verify(matcherClass(self.actual, *expectedValues).negated)

        setattr(cls, method_name, matcher_function)
        setattr(cls, negated_method_name, negated_matcher_function)


Expectation.addMatcher(matchers.ToBe)
Expectation.addMatcher(matchers.ToEqual)
Expectation.addMatcher(matchers.ToBeNone)
Expectation.addMatcher(matchers.ToBeTruthy)
Expectation.addMatcher(matchers.ToBeFalsy)
Expectation.addMatcher(matchers.ToMatch)
Expectation.addMatcher(matchers.ToContain)
Expectation.addMatcher(matchers.ToBeGreaterThan)
Expectation.addMatcher(matchers.ToBeLessThan)
Expectation.addMatcher(matchers.ToHaveBeenCalled)
