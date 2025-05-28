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
parse_nested_parens = getattr(module, "parse_nested_parens")

class TestParseNestedParens(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(""), [])

    def test_only_spaces(self):
        self.assertEqual(parse_nested_parens("  "), [])

    def test_single_paren(self):
        self.assertEqual(parse_nested_parens("()"), [1])

    def test_multiple_paren(self):
        self.assertEqual(parse_nested_parens("() () ()"), [1, 1, 1])

    def test_complex(self):
        self.assertEqual(parse_nested_parens("() ((())) (()) (((()(()))))"), [1, 3, 2, 5])

    def test_unnecessary_spaces(self):
        self.assertEqual(parse_nested_parens("  (()())   ((()))  "), [2, 3])

if __name__ == "__main__":
    unittest.main()
