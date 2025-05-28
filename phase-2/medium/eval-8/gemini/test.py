import unittest
from typing import List, Tuple
from generated_code import sum_product # Uncomment this if the function is in solution.py


class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        """Test case for an empty list."""
        self.assertEqual(sum_product([]), (0, 1))

    def test_positive_integers(self):
        """Test case with only positive integers."""
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))
        self.assertEqual(sum_product([5, 10]), (15, 50))

    def test_with_zero(self):
        """Test case including zero."""
        self.assertEqual(sum_product([1, 2, 0, 4]), (7, 0))
        self.assertEqual(sum_product([0]), (0, 0))

    def test_negative_integers(self):
        """Test case with only negative integers."""
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))
        self.assertEqual(sum_product([-2, -4]), (-6, 8))

    def test_mixed_integers(self):
        """Test case with a mix of positive, negative, and zero."""
        self.assertEqual(sum_product([-1, 2, -3, 0, 5]), (3, 0))
        self.assertEqual(sum_product([-1, 2, 3, -4]), (0, 24))


# To run the tests, save this code as a Python file (e.g., test_sum_product.py)
# and run it from your terminal: python -m unittest test_sum_product.py
# Make sure the sum_product function definition is in the same file or imported correctly.

if __name__ == "__main__":
    unittest.main()
