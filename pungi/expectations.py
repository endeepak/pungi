__unittest = True


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

        def matcher_function(self, *expectedArgs, **expectedKwArgs):
            self.verify(matcherClass(self.actual, *expectedArgs,
                                    **expectedKwArgs))

        def negated_matcher_function(self, *expectedArgs, **expectedKwArgs):
            self.verify(matcherClass(self.actual, *expectedArgs,
                                                 **expectedKwArgs).negated)

        setattr(cls, method_name, matcher_function)
        setattr(cls, negated_method_name, negated_matcher_function)
