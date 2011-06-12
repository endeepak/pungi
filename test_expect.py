import unittest
from pungi import expect


class ExpectTest(unittest.TestCase):

    def test_to_be_when_assertion_passes(self):
        expect(True).toBe(True)

    def test_to_be_when_assertion_fails(self):
        self.assertRaises(AssertionError, expect(True).toBe, False)

    def test_not_to_be_when_assertion_passes(self):
        expect(True).notToBe(False)

    def test_not_to_be_when_assertion_fails(self):
        self.assertRaises(AssertionError, expect(True).notToBe, True)


if __name__ == '__main__':
    unittest.main()
