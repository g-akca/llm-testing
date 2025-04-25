import unittest

# The function under test is assumed to live in a file named `solution.py`
from code import by_length


class TestByLength(unittest.TestCase):
    def test_typical_case(self):
        """Digits 1-9 are kept, sorted, reversed, and mapped to words."""
        data = [2, 1, 1, 4, 5, 8, 2, 3]
        expected = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
        self.assertEqual(by_length(data), expected)

    def test_empty_list(self):
        """Empty input should return an empty list."""
        self.assertEqual(by_length([]), [])

    def test_ignore_non_digit_and_out_of_range(self):
        """Values outside 1-9 (or non-ints) are ignored."""
        data = [1, -5, 0, 10, 3.5, 9]
        expected = ["Nine", "One"]
        self.assertEqual(by_length(data), expected)

    def test_all_filtered_out(self):
        """If every element is filtered out, result should be empty."""
        data = [-1, 0, 12, 100]
        self.assertEqual(by_length(data), [])


if __name__ == "__main__":
    unittest.main()
