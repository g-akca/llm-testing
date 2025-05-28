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
mean_absolute_deviation = getattr(module, "mean_absolute_deviation")

""" For a given list of input numbers, calculate Mean Absolute Deviation
around the mean of this dataset.
Mean Absolute Deviation is the average absolute difference between each
element and a centerpoint (mean in this case):
MAD = average | x - x_mean |
>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
"""

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0)

    def test_single_element(self):
        self.assertEqual(mean_absolute_deviation([5]), 0)

    def test_mixed_negative_positive(self):
        self.assertEqual(mean_absolute_deviation([-3, 0, 3]), 2)

    def test_same_elements(self):
        self.assertEqual(mean_absolute_deviation([5, 5, 5, 5]), 0)

if __name__ == "__main__":
    unittest.main()
