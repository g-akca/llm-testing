import unittest

# Adjust the import path to match where `fix_spaces` is defined.
# If your implementation is in, e.g., solution.py, use:
#     from solution import fix_spaces
from generated_code import fix_spaces   # rename as needed


class FixSpacesTests(unittest.TestCase):
    def test_no_spaces(self):
        self.assertEqual(fix_spaces("Example"), "Example")

    def test_single_space(self):
        self.assertEqual(fix_spaces("Example 1"), "Example_1")

    def test_leading_single_space(self):
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")

    def test_leading_and_three_spaces(self):
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

    def test_middle_three_spaces(self):
        self.assertEqual(fix_spaces("hello   world"), "hello-world")


if __name__ == "__main__":
    unittest.main()
