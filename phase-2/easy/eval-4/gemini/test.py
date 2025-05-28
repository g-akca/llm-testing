import unittest
from typing import List
import math # Keep the import from the original code for context, though not used here

# Assuming the function mean_absolute_deviation is in a file named 'mad_calculator.py'
# If it's in the same file, you don't need the import line below.
from generated_code import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_basic_case(self):
        """ Test the example provided in the docstring. """
        self.assertAlmostEqual(
            mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0
        )

    def test_empty_list(self):
        """ Test with an empty list. """
        self.assertAlmostEqual(mean_absolute_deviation([]), 0.0)

    def test_identical_elements(self):
        """ Test with a list where all elements are the same. """
        self.assertAlmostEqual(
            mean_absolute_deviation([5.0, 5.0, 5.0, 5.0]), 0.0
        )

    def test_with_negative_numbers(self):
        """ Test with a list containing negative numbers. """
        # Mean = (-2 + 0 + 2 + 4) / 4 = 4 / 4 = 1.0
        # Deviations = |-2 - 1|, |0 - 1|, |2 - 1|, |4 - 1|
        #            = |-3|, |-1|, |1|, |3|
        #            = 3, 1, 1, 3
        # MAD = (3 + 1 + 1 + 3) / 4 = 8 / 4 = 2.0
        self.assertAlmostEqual(
            mean_absolute_deviation([-2.0, 0.0, 2.0, 4.0]), 2.0
        )

    def test_single_element(self):
        """ Test with a list containing only one element. """
        self.assertAlmostEqual(mean_absolute_deviation([10.5]), 0.0)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
