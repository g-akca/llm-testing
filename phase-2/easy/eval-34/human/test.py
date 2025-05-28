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
unique = getattr(module, "unique")

"""Return sorted unique elements in a list
>>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
[0, 2, 3, 5, 9, 123]
"""

class TestUnique(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(unique([]), [])

    def test_with_no_duplicates(self):
        self.assertEqual(unique([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_with_all_duplicates(self):
        self.assertEqual(unique([7, 7, 7]), [7])

    def test_with_negative_and_zero(self):
        self.assertEqual(unique([-2, -1, 0, -2, 0]), [-2, -1, 0])

    def test_with_duplicates_and_unsorted_elements(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

if __name__ == "__main__":
    unittest.main()
