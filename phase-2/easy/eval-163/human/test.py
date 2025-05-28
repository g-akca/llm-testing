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
generate_integers = getattr(module, "generate_integers")

"""
Given two positive integers a and b, return the even digits between a
and b, in ascending order.

For example:
generate_integers(2, 8) => [2, 4, 6, 8]
generate_integers(8, 2) => [2, 4, 6, 8]
generate_integers(10, 14) => []
"""

class TestGenerateIntegers(unittest.TestCase):
    def test_same_numbers(self):
        self.assertEqual(generate_integers(2, 2), [2])
        self.assertEqual(generate_integers(3, 3), [])

    def test_descending_range(self):
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])
    
    def test_ascending_range(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_no_even_digits(self):
        self.assertEqual(generate_integers(10, 14), [])
        self.assertEqual(generate_integers(15, 24), [])

if __name__ == "__main__":
    unittest.main()
