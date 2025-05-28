import unittest

# Assuming the implementation is saved in `sort_numbers.py`
from generated_code import sort_numbers


class TestSortNumbers(unittest.TestCase):
    def test_basic_example(self):
        """Example in the docstring."""
        self.assertEqual(sort_numbers("three one five"), "one three five")

    def test_with_duplicates(self):
        """Handles repeated values correctly."""
        self.assertEqual(
            sort_numbers("seven three three zero"),
            "zero three three seven",
        )

    def test_extremes(self):
        """Sorts smallest and largest correctly."""
        self.assertEqual(sort_numbers("nine zero"), "zero nine")

    def test_empty_input(self):
        """Returns an empty string for empty input."""
        self.assertEqual(sort_numbers(""), "")

    def test_invalid_token(self):
        """Raises ValueError on unrecognized number words."""
        with self.assertRaises(ValueError):
            sort_numbers("three uno five")  # 'uno' is invalid


if __name__ == "__main__":
    unittest.main()
