import unittest
import pungi
import pungi.dec


class TempClass(object):

    def hello(self):
        return "hello"


class MethodDecoratorTest(unittest.TestCase):

    def setUp(self):
        self.obj = TempClass()

    @pungi.dec.test
    def test_spied_decorator_stops_spying_after_running_the_test(self):
        pungi.spyOn(self.obj, 'hello', returnValue="spy says hello")

        self.assertEqual(self.obj.hello(), "spy says hello")

    def tearDown(self):
        self.assertEqual(self.obj.hello(), "hello",
                        "Decorator did not stop spying!!")


@pungi.dec.testcase
class ClassDecoratorTest(unittest.TestCase):

    def setUp(self):
        self.obj = TempClass()

    def test_spied_decorator_stops_spying_after_running_the_test(self):
        pungi.spyOn(self.obj, 'hello', returnValue="spy says hello")

        self.assertEqual(self.obj.hello(), "spy says hello")

    def tearDown(self):
        self.assertEqual(self.obj.hello(), "hello",
                        "Decorator did not stop spying!!")


if __name__ == '__main__':
    unittest.main()
