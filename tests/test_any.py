import unittest
from pungi import Any


class TestAny(unittest.TestCase):

    def test_eq(self):
        self.assertEqual(1, Any(int))
        self.assertEqual(True, Any(bool))
        self.assertEqual(1.1, Any(float))
        self.assertEqual('1', Any(str))
        self.assertEqual({}, Any(dict))
        self.assertEqual([1], Any(list))
        self.assertNotEqual(True, Any(int))
        self.assertNotEqual('1', Any(int))


if __name__ == '__main__':
    unittest.main()
