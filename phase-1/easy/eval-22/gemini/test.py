import unittest
from typing import List, Any
from generated_code import filter_integers


class TestFilterIntegers(unittest.TestCase):

    def test_mixed_list(self):
        """Test filtering a list with mixed data types."""
        self.assertEqual(filter_integers(['a', 3.14, 5, None, [1], {}]), [5])

    def test_only_integers(self):
        """Test filtering a list containing only integers."""
        self.assertEqual(filter_integers([1, 2, 3, -4, 0]), [1, 2, 3, -4, 0])

    def test_no_integers(self):
        """Test filtering a list containing no integers."""
        self.assertEqual(filter_integers(['a', 'b', 3.14, 2.71, None, []]), [])

    def test_empty_list(self):
        """Test filtering an empty list."""
        self.assertEqual(filter_integers([]), [])

    def test_with_booleans(self):
        """Test filtering a list containing booleans (which are instances of int)."""
        # Note: isinstance(True, int) is True, isinstance(False, int) is True
        self.assertEqual(filter_integers([1, True, 0, False, 'abc']), [1, True, 0, False])

# To run the tests:
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
