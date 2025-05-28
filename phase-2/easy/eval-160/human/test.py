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
do_algebra = getattr(module, "do_algebra")

"""
Given two lists operator, and operand. The first list has basic algebra operations, and 
the second list is a list of integers. Use the two given lists to build the algebric 
expression and return the evaluation of this expression.

The basic algebra operations:
Addition ( + ) 
Subtraction ( - ) 
Multiplication ( * ) 
Floor division ( // ) 
Exponentiation ( ** ) 

Example:
operator['+', '*', '-']
array = [2, 3, 4, 5]
result = 2 + 3 * 4 - 5
=> result = 9

Note:
    The length of operator list is equal to the length of operand list minus one.
    Operand is a list of of non-negative integers.
    Operator list has at least one operator, and operand list has at least two operands.

"""

class TestDoAlgebra(unittest.TestCase):
    def test_basic_mixed_ops(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)
    
    def test_exponent_then_add(self):
        self.assertEqual(do_algebra(['**', '+'], [2, 3, 1]), 9)

    def test_floor_division(self):
        self.assertEqual(do_algebra(['//', '-'], [10, 3, 1]), 2)

if __name__ == "__main__":
    unittest.main()
