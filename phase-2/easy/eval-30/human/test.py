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
get_positive = getattr(module, "get_positive")

"""Return only positive numbers in the list.
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
"""

class TestGetPositive(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_positive([]), [])

    def test_positive_numbers(self):
        self.assertEqual(get_positive([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(get_positive([-1, -2, -3, -4, -5]), [])

    def test_mixed_numbers(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6, -3, 3, 9, 0, 123, 1, -10]), [2, 5, 6, 3, 9, 123, 1])

    def test_zero(self):
        self.assertEqual(get_positive([0]), [])

if __name__ == "__main__":
    unittest.main()
