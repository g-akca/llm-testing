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
split_words = getattr(module, "split_words")

class TestSplitWords(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(split_words(""), 0)

    def test_whitespace_split(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_comma_split(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_odd_lowercase_count(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_whitespace_priority_over_comma(self):
        self.assertEqual(split_words("Hello, world,again"), ["Hello,", "world,again"])

if __name__ == "__main__":
    unittest.main()
