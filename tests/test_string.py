import unittest
from pungi import string
from pungi import expect


class StringTest(unittest.TestCase):

    def test_pp_with_no_args(self):
        expect(string.pp()).toBe("")

    def test_pp_of_single_arg(self):
        expect(string.pp('1')).toBe("'1'")
        expect(string.pp(1)).toBe("1")

    def test_pp_of_multiple_args(self):
        expect(string.pp(1, 2)).toBe("1, 2")
        expect(string.pp(1, [2, 3])).toBe("1, [2, 3]")

    def test_humanize_camelcase_word(self):
        expect(string.humanize("SomeOne")).toBe("some one")
        expect(string.humanize("SomeOneElse")).toBe("some one else")


if __name__ == '__main__':
    unittest.main()
