import unittest
from typing import List, Tuple

# Assuming the function is defined in a module named `main`.
# If your function lives elsewhere (e.g., `from my_module import sum_product`),
# adjust the import accordingly.
from code import sum_product


class TestSumProduct(unittest.TestCase):
    def test_empty_list(self):
        """Empty list should return (0, 1)."""
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element(self):
        """Single-element list should return the element itself for both sum and product."""
        self.assertEqual(sum_product([7]), (7, 7))

    def test_positive_numbers(self):
        """List of positive integers should return correct sum and product."""
        numbers = [1, 2, 3, 4]
        expected: Tuple[int, int] = (10, 24)
        self.assertEqual(sum_product(numbers), expected)

    def test_including_zero(self):
        """If the list contains zero, product should be zero while sum should be correct."""
        numbers = [5, 0, 2]
        expected: Tuple[int, int] = (7, 0)
        self.assertEqual(sum_product(numbers), expected)

    def test_negative_numbers(self):
        """List with negative integers should handle sum and product correctly."""
        numbers = [-1, -2, -3]
        expected: Tuple[int, int] = (-6, -1 * -2 * -3)  # -6, -6
        self.assertEqual(sum_product(numbers), expected)


if __name__ == "__main__":
    unittest.main()
