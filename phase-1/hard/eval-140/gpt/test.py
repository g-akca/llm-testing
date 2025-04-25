import unittest

from generated_code import fix_spaces   # adjust the import path if needed


class TestFixSpaces(unittest.TestCase):
    def test_no_spaces(self):
        self.assertEqual(fix_spaces("Example"), "Example")

    def test_single_space(self):
        self.assertEqual(fix_spaces("Example 1"), "Example_1")

    def test_leading_and_double_space(self):
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")

    def test_triple_space(self):
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

    def test_only_spaces(self):
        # three spaces should collapse to a single hyphen
        self.assertEqual(fix_spaces("   "), "-")


if __name__ == "__main__":
    unittest.main()
