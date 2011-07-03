import unittest
from pungi import expect
from pungi import spyOn


class TempClass(object):

    def hello(self):
        return "hello"


class CustomException(Exception):
    pass


class TestMatchers(unittest.TestCase):

    def test_toBe(self):
        expect(True).toBe(True)
        expect(True).notToBe(False)

        self.assertRaises(AssertionError, expect(True).toBe, False)
        self.assertRaises(AssertionError, expect(True).notToBe, True)

    def test_toEqual(self):
        expect(True).toEqual(True)
        expect(True).notToEqual(False)

        self.assertRaises(AssertionError, expect(True).toEqual, False)
        self.assertRaises(AssertionError, expect(True).notToEqual, True)

    def test_toBeNone(self):
        expect(None).toBeNone()
        expect('foo').notToBeNone()

        self.assertRaises(AssertionError, expect('foo').toBeNone)
        self.assertRaises(AssertionError, expect(None).notToBeNone)

    def test_toBeTruthy(self):
        expect(True).toBeTruthy()
        expect('foo').notToBeTruthy()

        self.assertRaises(AssertionError, expect('foo').toBeTruthy)
        self.assertRaises(AssertionError, expect(True).notToBeTruthy)

    def test_toBeFalsy(self):
        expect(False).toBeFalsy()
        expect('foo').notToBeFalsy()

        self.assertRaises(AssertionError, expect('foo').toBeFalsy)
        self.assertRaises(AssertionError, expect(False).notToBeFalsy)

    def test_toMatch(self):
        expect("abcd").toMatch(".*b.*")
        expect("abcd").notToMatch(".*g.*")

        self.assertRaises(AssertionError, expect("abcd").toMatch, ".*g.*")
        self.assertRaises(AssertionError, expect("abcd").notToMatch, ".*b.*")

    def test_toContain_for_String(self):
        expect("abcd").toContain("b")
        expect("abcd").notToContain("f")

        self.assertRaises(AssertionError, expect("abcd").toContain, "f")
        self.assertRaises(AssertionError, expect("abcd").notToContain, "b")

    def test_toContain_for_Array(self):
        expect([1, 2, 3]).toContain(2)
        expect([1, 2, 3]).notToContain(4)

        self.assertRaises(AssertionError, expect([1, 2, 3]).toContain, 4)
        self.assertRaises(AssertionError, expect([1, 2, 3]).notToContain, 2)

    def test_toBeGreaterThan(self):
        expect(2).toBeGreaterThan(1)
        expect(1).notToBeGreaterThan(2)

        self.assertRaises(AssertionError, expect(1).toBeGreaterThan, 2)
        self.assertRaises(AssertionError, expect(2).notToBeGreaterThan, 1)

    def test_toBeLessThan(self):
        expect(1).toBeLessThan(2)
        expect(2).notToBeLessThan(1)

        self.assertRaises(AssertionError, expect(2).toBeLessThan, 1)
        self.assertRaises(AssertionError, expect(1).notToBeLessThan, 2)

    def test_ToRaiseException(self):
        def raise_ex():
            raise CustomException

        def dont_raise_ex():
            pass

        expect(raise_ex).toRaise(CustomException)
        expect(dont_raise_ex).notToRaise(CustomException)

        self.assertRaises(AssertionError, expect(dont_raise_ex).toRaise, CustomException)
        self.assertRaises(AssertionError, expect(raise_ex).notToRaise, CustomException)

    def test_ToRaiseExceptionWithMessage(self):
        def raise_ex():
            raise CustomException("<(^_^)>")

        def dont_raise_ex():
            pass

        expect(raise_ex).toRaise(Exception, "<(^_^)>")
        expect(dont_raise_ex).notToRaise(Exception)

        self.assertRaises(AssertionError, expect(dont_raise_ex).toRaise, Exception, "<(^_^)>")
        self.assertRaises(AssertionError, expect(raise_ex).toRaise, Exception, "[(-.-)]")

        self.assertRaises(AssertionError, expect(raise_ex).notToRaise, Exception)

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

    def test_toHaveBeenCalledTimes(self):
        obj = TempClass()
        spyOn(obj, 'hello')

        obj.hello()
        obj.hello()

        expect(obj.hello).toHaveBeenCalled(times=2)
        self.assertRaises(AssertionError,
                          expect(obj.hello).toHaveBeenCalled, times=1)

    def test_toHaveBeenCalledWith(self):
        obj = TempClass()
        spyOn(obj, 'hello')
        spyOn(obj, 'hi')
        obj.hello(1, to=2)

        expect(obj.hello).toHaveBeenCalledWith(1, to=2)
        expect(obj.hi).notToHaveBeenCalledWith(1, to=2)

        self.assertRaises(AssertionError,
                          expect(obj.hello).notToHaveBeenCalledWith, 1, to=2)
        self.assertRaises(AssertionError,
                          expect(obj.hi).toHaveBeenCalledWith, 1, to=2)


if __name__ == '__main__':
    unittest.main()
