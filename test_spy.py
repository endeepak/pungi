import unittest
from pungi import spyOn
from pungi import expect


class TempClass(object):

    def hello(self):
        return "hello"


class SpyUsageTest(unittest.TestCase):

    def test_method_call_assertion(self):
        obj = TempClass()

        with spyOn(obj, 'hello'):
            obj.hello()
            expect(obj.hello).toHaveBeenCalled()

    def test_return_value(self):
        obj = TempClass()

        with spyOn(obj, 'hello', returnValue="new hello"):
            expect(obj.hello()).toBe("new hello")

    def test_spies_are_cleared_after_exiting_with_statement(self):
        obj = TempClass()

        with spyOn(obj, 'hello', returnValue="new hello"):
            expect(obj.hello()).toBe("new hello")

        expect(obj.hello()).toBe("hello")


if __name__ == '__main__':
    unittest.main()
