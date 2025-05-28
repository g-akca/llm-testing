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
filter_integers = getattr(module, "filter_integers")

""" Filter given list of any python values only for integers
>>> filter_integers(['a', 3.14, 5])
[5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
[1, 2, 3]
"""

class TestFilterIntegers(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_integers([]), [])

    def test_mixed_list(self):
        self.assertEqual(filter_integers(['a', 3.14, 5, None, [1], {}]), [5])
    
    def test_only_integers(self):
        self.assertEqual(filter_integers([1, 2, 3, -4, 0]), [1, 2, 3, -4, 0])
    
    def test_no_integers(self):
        self.assertEqual(filter_integers(['a', 'b', 3.14, 2.71, None, []]), [])
    
    def test_with_booleans(self):
        self.assertEqual(filter_integers([1, True, 0, False]), [1, 0])

if __name__ == "__main__":
    unittest.main()
