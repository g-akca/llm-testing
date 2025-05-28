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
correct_bracketing = getattr(module, "correct_bracketing")

class TestCorrectBracketing(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(correct_bracketing(""), True)
    
    def test_single_open(self):
        self.assertFalse(correct_bracketing("("))
    
    def test_simple_pair(self):
        self.assertTrue(correct_bracketing("()"))
    
    def test_nested_balanced(self):
        self.assertTrue(correct_bracketing("(()())"))

    def test_unbalanced_close_first(self):
        self.assertFalse(correct_bracketing(")(()"))

if __name__ == "__main__":
    unittest.main()
