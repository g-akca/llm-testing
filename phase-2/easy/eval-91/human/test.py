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
is_bored = getattr(module, "is_bored")

"""
You'll be given a string of words, and your task is to count the number
of boredoms. A boredom is a sentence that starts with the word "I".
Sentences are delimited by '.', '?' or '!'.

For example:
>>> is_bored("Hello world")
0
>>> is_bored("The sky is blue. The sun is shining. I love this weather")
1
"""

class TestIsBored(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_no_boredoms(self):
        text = "Hello world. How are you today?"
        self.assertEqual(is_bored(text), 0)
    
    def test_single_boredom(self):
        text = "The sky is blue. The sun is shining. I love this weather"
        self.assertEqual(is_bored(text), 1)
    
    def test_multiple_boredoms(self):
        text = "I am bored! Why is that? I do not know. Maybe tomorrow."
        self.assertEqual(is_bored(text), 2)

    def test_leading_trailing_spaces(self):
        text = "   I am happy.  But I am also tired. "
        self.assertEqual(is_bored(text), 1)
    
    def test_empty_and_no_sentence_strings(self):
        self.assertEqual(is_bored(""), 0)
        self.assertEqual(is_bored("      "), 0)

if __name__ == "__main__":
    unittest.main()
