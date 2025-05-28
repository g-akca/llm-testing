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
reverse_delete = getattr(module, "reverse_delete")

"""Task
We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
then check if the result string is palindrome.
A string is called palindrome if it reads the same backward as forward.
You should return a tuple containing the result string and True/False for the check.
Example
For s = "abcde", c = "ae", the result should be ('bcd',False)
For s = "abcdef", c = "b"  the result should be ('acdef',False)
For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
"""

class TestReverseDelete(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_delete("", ""), ("", True))

    def test_empty_c_string(self):
        self.assertEqual(reverse_delete("level", ""), ("level", True))
        self.assertEqual(reverse_delete("python", ""), ("python", False))
    
    def test_empty_s_string(self):
        self.assertEqual(reverse_delete("", "abc"), ("", True))
    
    def test_all_chars_removed(self):
        self.assertEqual(reverse_delete("aaaa", "a"), ("", True))
    
    def test_no_chars_removed(self):
        self.assertEqual(reverse_delete("abcde", ""), ("abcde", False))

if __name__ == "__main__":
    unittest.main()
