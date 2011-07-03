import unittest
from pungi import spy
from pungi import spyOn
from pungi import expect


class TempClass(object):

    def hello(self):
        return "hello"


class SpyMethodTest(unittest.TestCase):

    def test_return_value(self):
        obj = TempClass()

        spyOn(obj, 'hello', returnValue="spy says hello")

        self.assertEqual(obj.hello(), "spy says hello")

    def test_return_value_for_andReturn_syntax(self):
        obj = TempClass()

        spyOn(obj, 'hello').andReturn("spy says hello")

        self.assertEqual(obj.hello(), "spy says hello")

    def test_call_count_before_call(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        self.assertEqual(obj.hello.callCount, 0)

    def test_call_count_after_call(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        obj.hello()
        obj.hello()

        self.assertEqual(obj.hello.callCount, 2)

    def test_was_called_before_call(self):
        obj = TempClass()

        spyOn(obj, 'hello')

        self.assertFalse(obj.hello.wasCalled())

    def test_was_called_after_call(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        obj.hello()

        self.assertTrue(obj.hello.wasCalled())

    def test_was_called_times(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        obj.hello()
        obj.hello()

        self.assertTrue(obj.hello.wasCalled(times=2))

    def test_was_called_with(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        obj.hello(1)
        obj.hello(1, to=2)

        self.assertTrue(obj.hello.wasCalledWith(1))
        self.assertTrue(obj.hello.wasCalledWith(1, to=2))
        self.assertFalse(obj.hello.wasCalledWith(2))

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
        self.assertEqual(obj.hello.callCount, 1)

    def test_call_through_for_andCallThrough_syntax(self):
        obj = TempClass()

        spyOn(obj, 'hello').andCallThrough()

        self.assertEqual(obj.hello(), "hello")
        self.assertEqual(obj.hello.callCount, 1)

    def test_call_fake(self):
        obj = TempClass()

        def fake_hello():
            return "fake hello"

        spyOn(obj, 'hello', callFake=fake_hello)

        self.assertEqual(obj.hello(), "fake hello")
        self.assertEqual(obj.hello.callCount, 1)

    def test_call_fake_for_andCallFakeSyntax(self):
        obj = TempClass()

        def fake_hello():
            return "fake hello"

        spyOn(obj, 'hello').andCallFake(fake_hello)

        self.assertEqual(obj.hello(), "fake hello")
        self.assertEqual(obj.hello.callCount, 1)

    def test_most_recent_call_args(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        obj.hello("h", "e", "l", "l", "o")

        self.assertEqual(obj.hello.mostRecentCall.args,
                        ("h", "e", "l", "l", "o"))

    def test_most_recent_call_kwargs(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        obj.hello(say="hello")

        self.assertEqual(obj.hello.mostRecentCall.kwargs, dict(say="hello"))

    def test_args_for_call(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        obj.hello("h", "e")
        obj.hello("l", "l", "o")

        self.assertEqual(obj.hello.argsForCall(0), ("h", "e"))
        self.assertEqual(obj.hello.argsForCall(1), ("l", "l", "o"))

    def test_kwargs_for_call(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        obj.hello(say="hello")
        obj.hello(to="world")

        self.assertEqual(obj.hello.kwargsForCall(0), dict(say="hello"))
        self.assertEqual(obj.hello.kwargsForCall(1), dict(to="world"))

    def test_stop(self):
        obj = TempClass()
        spyOn(obj, 'hello', returnValue="spy says helloe")

        spy.Method.stop()

        self.assertEqual(obj.hello(), "hello")

    def test_repr(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        self.assertEqual(repr(obj.hello), "{0}.hello".format(repr(obj)))

if __name__ == '__main__':
    unittest.main()
