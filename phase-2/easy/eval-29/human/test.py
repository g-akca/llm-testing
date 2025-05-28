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
filter_by_prefix = getattr(module, "filter_by_prefix")

""" Filter an input list of strings only for ones that start with a given prefix.
>>> filter_by_prefix([], 'a')
[]
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
"""

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], "a"), [])
    
    def test_empty_prefix(self):
        self.assertEqual(filter_by_prefix(["alpha", "beta"], ""), ["alpha", "beta"])
    
    def test_no_match(self):
        self.assertEqual(filter_by_prefix(["foo", "bar", "baz"], "qux"), [])
    
    def test_all_matches(self):
        self.assertEqual(filter_by_prefix(["apple", "apricot", "application"], "app"), ["apple", "application"])

    def test_case_sensitivity(self):
        self.assertEqual(filter_by_prefix(["Apple", "apple", "Apricot", "apricot"], "A"), ["Apple", "Apricot"])

if __name__ == "__main__":
    unittest.main()
