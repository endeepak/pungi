import unittest
from pungi import createSpy


class SpyObjectTest(unittest.TestCase):

    def test_spy_respond_all_method(self):
        spyObj = createSpy('greeter')

        try:
            spyObj.hello()
        except AttributeError:
            self.fail("Spy Object did not respond")

    def test_spy_methods_are_tracked(self):
        spyObj = createSpy('greeter')

        spyObj.hello()

        self.assertEqual(spyObj.hello.callCount, 1)

    def test_spy_method_explicit_return_value(self):
        spyObj = createSpy('greeter')

        spyObj.hello.returnValue = "spy says hello"

        self.assertEqual(spyObj.hello(), "spy says hello")

    def test_spy_method_return_value(self):
        spyObj = createSpy('greeter', hello="say hello", hi="say hi")

        self.assertEqual(spyObj.hello(), "say hello")
        self.assertEqual(spyObj.hi(), "say hi")

    def test_str(self):
        self.assertEqual(str(createSpy('greeter')), "<spy name=greeter>")
        self.assertEqual(str(createSpy()), "<spy name=None>")


if __name__ == '__main__':
    unittest.main()
