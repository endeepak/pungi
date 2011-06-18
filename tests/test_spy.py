import unittest
from pungi import spyOn
from pungi import expect


class TempClass(object):

    def hello(self):
        return "hello"


class SpyTest(unittest.TestCase):

    def test_return_value(self):
        obj = TempClass()

        spyOn(obj, 'hello', returnValue="spy says hello")

        expect(obj.hello()).toBe("spy says hello")

    def test_return_value_for_andReturn_syntax(self):
        obj = TempClass()

        spyOn(obj, 'hello').andReturn("spy says hello")

        expect(obj.hello()).toBe("spy says hello")

    def test_call_count_before_call(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        self.assertEqual(obj.hello.callCount(), 0)

    def test_call_count_after_call(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        obj.hello()
        obj.hello()

        self.assertEqual(obj.hello.callCount(), 2)

    def test_was_called_before_call(self):
        obj = TempClass()

        spyOn(obj, 'hello')

        self.assertFalse(obj.hello.wasCalled())

    def test_was_called_before_call(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        obj.hello()

        self.assertTrue(obj.hello.wasCalled())

    def test_spy_is_on_inside_the_with_block(self):
        obj = TempClass()

        with spyOn(obj, 'hello', returnValue="spy says hello"):
            self.assertEqual(obj.hello(), "spy says hello")

    def test_spy_is_rolled_back_outside_the_with_block(self):
        obj = TempClass()

        with spyOn(obj, 'hello', returnValue="spy says hello"):
            pass

        self.assertEqual(obj.hello(), "hello")

    def test_raises_exception(self):
        obj = TempClass()

        spyOn(obj, 'hello', raiseException=Exception)

        self.assertRaises(Exception, obj.hello)

    def test_raises_exception_for_andRaise_syntax(self):
        obj = TempClass()

        spyOn(obj, 'hello').andRaise(Exception)

        self.assertRaises(Exception, obj.hello)

    def test_call_through(self):
        obj = TempClass()

        spyOn(obj, 'hello', callThrough=True)

        self.assertEqual(obj.hello(), "hello")
        self.assertEqual(obj.hello.callCount(), 1)

    def test_call_through_for_andCallThrough_syntax(self):
        obj = TempClass()

        spyOn(obj, 'hello').andCallThrough()

        self.assertEqual(obj.hello(), "hello")
        self.assertEqual(obj.hello.callCount(), 1)

    def test_call_fake(self):
        obj = TempClass()

        def fake_hello():
            return "fake hello"

        spyOn(obj, 'hello', callFake=fake_hello)

        self.assertEqual(obj.hello(), "fake hello")
        self.assertEqual(obj.hello.callCount(), 1)

    def test_call_fake_for_andCallFakeSyntax(self):
        obj = TempClass()

        def fake_hello():
            return "fake hello"

        spyOn(obj, 'hello').andCallFake(fake_hello)

        self.assertEqual(obj.hello(), "fake hello")
        self.assertEqual(obj.hello.callCount(), 1)


class SpyUsageTest(unittest.TestCase):

    def test_method_call_assertion(self):
        obj = TempClass()

        with spyOn(obj, 'hello'):
            obj.hello()
            expect(obj.hello).toHaveBeenCalled()

    def test_return_value(self):
        obj = TempClass()

        with spyOn(obj, 'hello', returnValue="spy says hello"):
            expect(obj.hello()).toBe("spy says hello")

    def test_spies_are_cleared_after_exiting_with_statement(self):
        obj = TempClass()

        with spyOn(obj, 'hello', returnValue="spy says hello"):
            expect(obj.hello()).toBe("spy says hello")

        expect(obj.hello()).toBe("hello")


if __name__ == '__main__':
    unittest.main()
