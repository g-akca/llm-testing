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
separate_paren_groups = getattr(module, "separate_paren_groups")

class TestSeparateParenGroups(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(separate_paren_groups(""), [])

    def test_only_spaces(self):
        self.assertEqual(separate_paren_groups("    "), [])

    def test_single_paren(self):
        self.assertEqual(separate_paren_groups("()"), ["()"])
        self.assertEqual(separate_paren_groups(" ( ) "), ["()"])

    def test_multiple_paren(self):
        self.assertEqual(separate_paren_groups("()()()"), ["()", "()", "()"])
        self.assertEqual(separate_paren_groups("( )   () (  )"), ["()", "()", "()"])

    def test_nested(self):
        self.assertEqual(separate_paren_groups("((()))"), ["((()))"])
        self.assertEqual(separate_paren_groups("(( (())) )"), ["(((())))"])

    def test_complex(self):
        self.assertEqual(separate_paren_groups("() (( ()) )(())(( (()(())))) "), ["()", "((()))", "(())", "(((()(()))))"])

if __name__ == "__main__":
    unittest.main()
