import unittest
import math
from regenerated_code import mean_absolute_deviation


class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_simple_exact_case(self):
        """Example from the docstring."""
        assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0


    def test_empty_list_returns_zero(self):
        """An empty dataset must have zero deviation."""
        assert mean_absolute_deviation([]) == 0.0


    def test_negative_and_positive_values(self):
        """MAD should handle values on both sides of zero symmetrically."""
        numbers = [-5, -1, 0, 1, 5]     # mean = 0
        expected = (5 + 1 + 0 + 1 + 5) / 5   # 2.4
        assert math.isclose(mean_absolute_deviation(numbers), expected, rel_tol=1e-9)


    def test_identical_values(self):
        """If all values are identical, deviation should be zero."""
        assert mean_absolute_deviation([7.7, 7.7, 7.7]) == 0.0

if __name__ == '__main__':
    unittest.main()
