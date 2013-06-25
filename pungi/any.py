class Any(object):
    def __init__(self, expectedObject):
        self.expectedObject = expectedObject

    def __eq__(self, other):
        return type(other) == self.expectedObject

    def __repr__(self):
        return "<{0}({1})>".format(__name__, self.expectedObject)
