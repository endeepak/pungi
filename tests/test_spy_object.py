import unittest
from pungi import createSpy


class SpyObjectTest(unittest.TestCase):

    def test_spy_respond_all_method(self):
        spy = createSpy('greeter')

        try:
            spy.hello()
        except AttributeError:
            self.fail("Spy did not respond")

    def test_spy_methods_are_tracked(self):
        spy = createSpy('greeter')

        spy.hello()

        self.assertEqual(spy.hello.callCount(), 1)

if __name__ == '__main__':
    unittest.main()
