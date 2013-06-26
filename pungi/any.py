class Any(object):
    def __init__(self, expectedClass):
        self.expectedClass = expectedClass

    def __eq__(self, other):
        return type(other) == self.expectedClass

    def __repr__(self):
        return "<{0}({1})>".format(__name__, self.expectedClass)
