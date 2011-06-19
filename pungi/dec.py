import pungi


def test(method):
    decorator = _decorate(method)
    return decorator


def testcase(cls):
    methods = cls.__dict__.keys()
    test_methods = filter(lambda name: name.startswith("test_"), methods)
    for method_name in test_methods:
        method = getattr(cls, method_name)
        decorator = _decorate(method)
        setattr(cls, method_name, decorator)
    return cls


def _decorate(method):

    def decorator(self):
        method(self)
        pungi.stopSpying()
    return decorator
