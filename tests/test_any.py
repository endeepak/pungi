import unittest
from pungi import any


class TestAny(unittest.TestCase):

    def test_eq(self):
        self.assertEqual(1, any(int))
        self.assertEqual(True, any(bool))
        self.assertEqual(1.1, any(float))
        self.assertEqual('1', any(str))
        self.assertEqual({}, any(dict))
        self.assertEqual([1], any(list))
        self.assertNotEqual(True, any(int))
        self.assertNotEqual('1', any(int))


if __name__ == '__main__':
    unittest.main()
