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
vowels_count = getattr(module, "vowels_count")

class TestVowelsCount(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(vowels_count(""), 0)

    def test_case_insensitive(self):
        self.assertEqual(vowels_count("OuCh"), 2)

    def test_standard_vowels(self):
        self.assertEqual(vowels_count("aeiouAEIOU"), 10)

    def test_y_at_end(self):
        self.assertEqual(vowels_count("beauty"), 4)

    def test_y_not_at_end(self):
        self.assertEqual(vowels_count("yellow"), 2)

if __name__ == "__main__":
    unittest.main()
