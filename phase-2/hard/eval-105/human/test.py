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
by_length = getattr(module, "by_length")

class TestByLength(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(by_length([]), [])

    def test_strange_number(self):
        self.assertEqual(by_length([50]), [])
        self.assertEqual(by_length([99, -2, 0]), [])
        self.assertEqual(by_length([1, 10, 155, 3, -8]), ["Three", "One"])
    
    def test_single_number(self):
        self.assertEqual(by_length([2]), ["Two"])
        self.assertEqual(by_length([9]), ["Nine"])

    def test_multiple_numbers(self):
        self.assertEqual(by_length([2, 6]), ["Six", "Two"])
        self.assertEqual(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 1]), ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "Two", "One", "One"])

if __name__ == "__main__":
    unittest.main()
