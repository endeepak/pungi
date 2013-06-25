import unittest
from pungi import expect
from pungi import spyOn
from pungi import Any


class TempClass(object):

    def hello(self):
        return "hello"


class CustomException(Exception):
    pass


class TestMatchers(unittest.TestCase):

    def test_toBe(self):
        obj = CustomException('Test')
        obj.data = {'foo': [{'bar': [True]}]}
        ex = CustomException('Test')
        ex.data = {'foo': [{'bar': [True]}]}

        expect(True).toBe(True)
        expect(obj).toBe(obj)
        expect(True).notToBe(False)
        expect(True).notToBe(1)
        expect(obj).notToBe(ex)
        expect(True).notToBe(Any(bool))

        self.assertRaises(AssertionError, expect(True).toBe, False)
        self.assertRaises(AssertionError, expect(True).toBe, 1)
        self.assertRaises(AssertionError, expect(obj).toBe, ex)
        self.assertRaises(AssertionError, expect(True).toBe, Any(bool))
        self.assertRaises(AssertionError, expect(True).notToBe, True)
        self.assertRaises(AssertionError, expect(obj).notToBe, obj)

    def test_toEqual(self):
        obj1 = CustomException('Test')
        obj1.data = {'foo': [{'bar': [True]}]}
        obj2 = CustomException('test')
        obj2.data = {'foo': [{'bar': [True]}]}
        obj3 = CustomException('Test')
        obj3.data = {'foo': [{'bar': [1]}]}
        ex = CustomException('Test')
        ex.data = {'foo': [{'bar': [True]}]}

        expect(True).toEqual(True)
        expect('foo').toEqual('foo')
        expect([True, False]).toEqual([True, False])
        expect([[True]]).toEqual([[True]])
        expect({'foo': [{'bar': [True]}]}).toEqual({'foo': [{'bar': [True]}]})
        expect(obj1).toEqual(ex)
        expect([True]).toEqual([Any(bool)])
        expect(True).notToEqual(False)
        expect('foo').notToEqual('bar')
        expect({'foo': [{'bar': [True]}]}).notToEqual(\
                {'foo': [{'bar': [False]}]})
        expect([True, False]).notToEqual([False, True])
        expect([True, False]).notToEqual([1, 0])
        expect([[True]]).notToEqual([[False]])
        expect(CustomException('Test')).notToEqual(ex)
        expect(obj2).notToEqual(ex)
        expect(obj3).notToEqual(ex)
        expect(True).notToEqual(Any(int))

        self.assertRaises(AssertionError, expect(True).toEqual, False)
        self.assertRaises(AssertionError, expect('foo').toEqual, 'bar')
        self.assertRaises(AssertionError,
                expect({'foo': [{'bar': [True]}]}).toEqual,
                {'foo': [{'bar': [False]}]})
        self.assertRaises(AssertionError,
                expect([True, False]).toEqual, [False, True])
        self.assertRaises(AssertionError, expect([True, False]).toEqual, [1, 0])
        self.assertRaises(AssertionError, expect([[True]]).toEqual, [[False]])
        self.assertRaises(AssertionError,
                expect(CustomException('Test')).toEqual, ex)
        self.assertRaises(AssertionError, expect(obj2).toEqual, ex)
        self.assertRaises(AssertionError, expect(obj3).toEqual, ex)
        self.assertRaises(AssertionError, expect(True).toEqual, Any(int))
        self.assertRaises(AssertionError, expect(True).notToEqual, True)
        self.assertRaises(AssertionError,
                expect([True, False]).notToEqual, [True, False])
        self.assertRaises(AssertionError, expect('foo').notToEqual, 'foo')
        self.assertRaises(AssertionError, expect([[True]]).notToEqual, [[True]])
        self.assertRaises(AssertionError,
                expect({'foo': [{'bar': [True]}]}).notToEqual,
                {'foo': [{'bar': [True]}]})
        self.assertRaises(AssertionError, expect(obj1).notToEqual, ex)
        self.assertRaises(AssertionError,
                expect([True]).notToEqual, [Any(bool)])

    def test_toBeNone(self):
        expect(None).toBeNone()
        expect('foo').notToBeNone()

        self.assertRaises(AssertionError, expect('foo').toBeNone)
        self.assertRaises(AssertionError, expect(None).notToBeNone)

    def test_toBeTruthy(self):
        expect(True).toBeTruthy()
        expect(1).toBeTruthy()
        expect('foo').toBeTruthy()
        expect([False]).toBeTruthy()
        expect({'foo': False}).toBeTruthy()
        expect(False).notToBeTruthy()
        expect(None).notToBeTruthy()
        expect(0).notToBeTruthy()
        expect('').notToBeTruthy()
        expect([]).notToBeTruthy()
        expect({}).notToBeTruthy()

        self.assertRaises(AssertionError, expect(False).toBeTruthy)
        self.assertRaises(AssertionError, expect(None).toBeTruthy)
        self.assertRaises(AssertionError, expect(0).toBeTruthy)
        self.assertRaises(AssertionError, expect('').toBeTruthy)
        self.assertRaises(AssertionError, expect([]).toBeTruthy)
        self.assertRaises(AssertionError, expect({}).toBeTruthy)
        self.assertRaises(AssertionError, expect(True).notToBeTruthy)
        self.assertRaises(AssertionError, expect('foo').notToBeTruthy)
        self.assertRaises(AssertionError, expect([False]).notToBeTruthy)
        self.assertRaises(AssertionError, expect({'foo': False}).notToBeTruthy)

    def test_toBeFalsy(self):
        expect(True).notToBeFalsy()
        expect(1).notToBeFalsy()
        expect('foo').notToBeFalsy()
        expect([False]).notToBeFalsy()
        expect({'foo': False}).notToBeFalsy()
        expect(False).toBeFalsy()
        expect(None).toBeFalsy()
        expect(0).toBeFalsy()
        expect('').toBeFalsy()
        expect([]).toBeFalsy()
        expect({}).toBeFalsy()

        self.assertRaises(AssertionError, expect(True).toBeFalsy)
        self.assertRaises(AssertionError, expect('foo').toBeFalsy)
        self.assertRaises(AssertionError, expect([False]).toBeFalsy)
        self.assertRaises(AssertionError, expect({'foo': False}).toBeFalsy)
        self.assertRaises(AssertionError, expect(False).notToBeFalsy)
        self.assertRaises(AssertionError, expect(None).notToBeFalsy)
        self.assertRaises(AssertionError, expect(0).notToBeFalsy)
        self.assertRaises(AssertionError, expect('').notToBeFalsy)
        self.assertRaises(AssertionError, expect([]).notToBeFalsy)
        self.assertRaises(AssertionError, expect({}).notToBeFalsy)

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

    def test_ToRaise(self):
        def raise_ex():
            raise CustomException

        def dont_raise_ex():
            pass

        expect(raise_ex).toRaise()
        expect(dont_raise_ex).notToRaise()

        self.assertRaises(AssertionError, expect(dont_raise_ex).toRaise)
        self.assertRaises(AssertionError, expect(raise_ex).notToRaise)

    def test_ToRaiseException(self):
        def raise_ex():
            raise CustomException

        def dont_raise_ex():
            pass

        expect(raise_ex).toRaise(CustomException)
        expect(dont_raise_ex).notToRaise(CustomException)

        self.assertRaises(AssertionError, expect(dont_raise_ex).toRaise,
                                            CustomException)
        self.assertRaises(AssertionError, expect(raise_ex).notToRaise,
                                            CustomException)

    def test_ToRaiseExceptionInstance(self):
        def raise_ex():
            ex = CustomException("<(^_^)>")
            ex.code = 1
            raise ex

        def dont_raise_ex():
            pass

        class TempException(Exception):
            pass

        ex = CustomException("<(^_^)>")
        ex.code = 1
        e = Exception("<(^_^)>")
        e.code = 1
        temp_ex = TempException("<(^_^)>")
        temp_ex.code = 1
        expect(raise_ex).toRaise(ex)
        expect(raise_ex).toRaise(e)
        expect(dont_raise_ex).notToRaise(ex)
        expect(raise_ex).notToRaise(temp_ex)
        expect(raise_ex).notToRaise(CustomException("<(^_^)>"))

        self.assertRaises(AssertionError, expect(dont_raise_ex).toRaise, ex)
        self.assertRaises(AssertionError, expect(raise_ex).toRaise, temp_ex)
        self.assertRaises(AssertionError, expect(raise_ex).toRaise,
                                                    CustomException("<(^_^)>"))
        self.assertRaises(AssertionError, expect(raise_ex).notToRaise, ex)
        self.assertRaises(AssertionError, expect(raise_ex).notToRaise, e)

    def test_ToRaiseExceptionWithMessage(self):
        def raise_ex():
            raise CustomException("<(^_^)>")

        def dont_raise_ex():
            pass

        expect(raise_ex).toRaise(Exception, "<(^_^)>")
        expect(dont_raise_ex).notToRaise(Exception)

        self.assertRaises(AssertionError, expect(dont_raise_ex).toRaise,
                                                    Exception, "<(^_^)>")
        self.assertRaises(AssertionError, expect(raise_ex).toRaise,
                                                    Exception, "[(-.-)]")

        self.assertRaises(AssertionError, expect(raise_ex).notToRaise,
                                                    Exception)

    def test_ToRaiseWithMessage(self):
        def raise_ex():
            raise CustomException("<(^_^)>")

        def dont_raise_ex():
            pass

        expect(raise_ex).toRaise(None, "<(^_^)>")
        expect(dont_raise_ex).notToRaise(None, "<(^_^)>")

        self.assertRaises(AssertionError, expect(dont_raise_ex).toRaise,
                                                    None, "<(^_^)>")
        self.assertRaises(AssertionError, expect(raise_ex).toRaise,
                                                    None, "[(-.-)]")

        self.assertRaises(AssertionError, expect(raise_ex).notToRaise)

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
        expect(obj.hello).toHaveBeenCalledWith(Any(int), to=Any(int))
        expect(obj.hi).notToHaveBeenCalledWith(1, to=2)
        expect(obj.hi).notToHaveBeenCalledWith(Any(bool), to=Any(bool))

        self.assertRaises(AssertionError,
                          expect(obj.hello).notToHaveBeenCalledWith, 1, to=2)
        self.assertRaises(AssertionError,
                          expect(obj.hello).notToHaveBeenCalledWith, Any(int),
                          to=Any(int))
        self.assertRaises(AssertionError,
                          expect(obj.hi).toHaveBeenCalledWith, 1, to=2)
        self.assertRaises(AssertionError,
                          expect(obj.hi).toHaveBeenCalledWith, Any(bool),
                          to=Any(bool))

    def test_toHaveBeenCalledBefore(self):
        obj = TempClass()
        spyOn(obj, 'hello')
        spyOn(obj, 'hi')

        obj.hi()
        obj.hello()

        expect(obj.hi).toHaveBeenCalledBefore(obj.hello)
        expect(obj.hello).notToHaveBeenCalledBefore(obj.hi)

        self.assertRaises(AssertionError,
                          expect(obj.hi).notToHaveBeenCalledBefore, obj.hello)
        self.assertRaises(AssertionError,
                          expect(obj.hello).toHaveBeenCalledBefore, obj.hi)


if __name__ == '__main__':
    unittest.main()
