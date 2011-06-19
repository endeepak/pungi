import pungi


def test(function):

    def decorator(self):
        function(self)
        pungi.stopSpying()
    return decorator

def testcase(cls):
    test_methods = filter(lambda name: name.startswith("test_"), cls.__dict__.keys())
    for method_name in test_methods:
        method = getattr(cls, method_name)
        def decorator(self):
            method(self)
            pungi.stopSpying()
        setattr(cls, method_name, decorator)
    return cls
