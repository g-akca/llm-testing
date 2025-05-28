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
sort_numbers = getattr(module, "sort_numbers")

class TestSortNumbers(unittest.TestCase):
    def test_empty_string(self):
        """Test case for an empty list."""
        self.assertEqual(sort_numbers(""), "")

    def test_single_number(self):
        """Test case for a single number."""
        self.assertEqual(sort_numbers("three"), "three")

    def test_multiple_numbers(self):
        """Test case for multiple numbers."""
        self.assertEqual(sort_numbers("nine eight seven six five four three two one zero"), "zero one two three four five six seven eight nine")

    def test_with_duplicates(self):
        """Test case for numbers with duplicates."""
        self.assertEqual(sort_numbers("one one two three three"), "one one two three three")

    def test_with_spaces(self):
        """Test case for numbers with spaces."""
        self.assertEqual(sort_numbers("six  two   nine "), "two six nine")

if __name__ == "__main__":
    unittest.main()
