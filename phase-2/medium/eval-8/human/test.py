# @Authors
# Student Names: Barış Türker, Gökçe Akca, Necip Baha Sağıroğlu
# Student IDs: 150170113, 150210046, 150220727

import sys
import os
import importlib
import unittest

if len(sys.argv) != 2 or sys.argv[1] not in ["gpt", "gemini"]:
    print("Usage: python test.py [gpt|gemini]")
    sys.exit(1)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
prompt = sys.argv.pop(1)
module_name = f"{prompt}.generated_code"
module = importlib.import_module(module_name)
sum_product = getattr(module, "sum_product")

class TestSumProduct(unittest.TestCase):
    def test_empty_list(self):
        """Test case for an empty list."""
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element(self):
        """Single-element list should return the element itself for both sum and product."""
        self.assertEqual(sum_product([7]), (7, 7))

    def test_positive_integers(self):
        """Test case with only positive integers."""
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_with_zero(self):
        """Test case including zero."""
        self.assertEqual(sum_product([1, 2, 0, 4]), (7, 0))

    def test_negative_integers(self):
        """Test case with only negative integers."""
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))

    def test_mixed_integers(self):
        """Test case with a mix of positive, negative, and zero."""
        self.assertEqual(sum_product([-1, 2, -3, 0, 5]), (3, 0))
        self.assertEqual(sum_product([-1, 2, 3, -4]), (0, 24))

if __name__ == "__main__":
    unittest.main()
