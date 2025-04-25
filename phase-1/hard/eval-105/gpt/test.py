import unittest

# Assuming `by_length` is defined in the same file; otherwise use:
from generated_code import by_length

class TestByLength(unittest.TestCase):
    def test_example_from_docstring(self):
        """Mixed valid digits should be sorted, reversed, and mapped correctly."""
        inp = [2, 1, 1, 4, 5, 8, 2, 3]
        expected = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
        self.assertEqual(by_length(inp), expected)

    def test_empty_list(self):
        """An empty input should return an empty list."""
        self.assertEqual(by_length([]), [])

    def test_ignores_invalid_numbers(self):
        """Numbers outside 1–9 are ignored after sorting/reversing."""
        inp = [1, -1, 55]
        expected = ["One"]
        self.assertEqual(by_length(inp), expected)

    def test_all_invalid_numbers(self):
        """If all numbers are invalid, the result should be empty."""
        inp = [-10, 0, 12, 100]
        self.assertEqual(by_length(inp), [])

if __name__ == "__main__":
    unittest.main()
