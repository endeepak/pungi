import unittest
from pungi import expect
from pungi import spyOn


class TempClass(object):

    def hello(self):
        return "hello"


class TestMatchers(unittest.TestCase):

    def test_toBe(self):
        expect(True).toBe(True)
        expect(True).notToBe(False)

        self.assertRaises(AssertionError, expect(True).toBe, False)
        self.assertRaises(AssertionError, expect(True).notToBe, True)

    def test_toHaveBeenCalled(self):
        obj = TempClass()
        spyOn(obj, 'hello')
        spyOn(obj, 'hi')
        obj.hello()

        expect(obj.hello).toHaveBeenCalled()
        expect(obj.hi).notToHaveBeenCalled()

        self.assertRaises(AssertionError,
                          expect(obj.hello).notToHaveBeenCalled)
        self.assertRaises(AssertionError,
                          expect(obj.hi).toHaveBeenCalled)


if __name__ == '__main__':
    unittest.main()
