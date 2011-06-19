import pungi


def test(method):
    return _decorated(method)


def testcase(cls):
    methods = cls.__dict__.keys()
    test_methods = filter(lambda name: name.startswith("test_"), methods)
    for method_name in test_methods:
        _decorate(cls, method_name)
    return cls


def _decorate(cls, method_name):
    method = getattr(cls, method_name)
    setattr(cls, method_name, _decorated(method))


def _decorated(method):

    def decorator(self):
        method(self)
        pungi.stopSpying()
    return decorator
