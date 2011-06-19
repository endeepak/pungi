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
