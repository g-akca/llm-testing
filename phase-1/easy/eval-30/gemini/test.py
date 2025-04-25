import unittest
from generated_code import get_positive

class TestGetPositive(unittest.TestCase):

    def test_empty_list(self):
        """Test that an empty list returns an empty list."""
        self.assertEqual(get_positive([]), [])

    def test_all_negative(self):
        """Test a list containing only negative numbers."""
        self.assertEqual(get_positive([-1, -5, -100, -3]), [])

    def test_all_positive(self):
        """Test a list containing only positive numbers."""
        self.assertEqual(get_positive([1, 5, 100, 3]), [1, 5, 100, 3])

    def test_mixed_with_zero(self):
        """Test a list containing positive, negative, and zero."""
        self.assertEqual(get_positive([-2, 0, 3, -5, 8, 0, 1]), [3, 8, 1])

    def test_from_doctest_1(self):
        """Test the first example from the docstring."""
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
