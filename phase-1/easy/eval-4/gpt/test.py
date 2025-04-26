import unittest
from code import mean_absolute_deviation   # adjust if your filename differs


class MeanAbsoluteDeviationTests(unittest.TestCase):

    def test_typical_sequence(self):
        """MAD of a simple ascending list is 1.0."""
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_singleton(self):
        """A single value should always give MAD = 0."""
        self.assertEqual(mean_absolute_deviation([5]), 0.0)

    def test_mixed_negative_positive(self):
        """Handles negative numbers and returns correct floating-point result."""
        result = mean_absolute_deviation([-2, 0, 2])       # mean = 0, MAD = (2+0+2)/3 = 1.333…
        self.assertAlmostEqual(result, 4/3, places=7)

    def test_empty_input_raises(self):
        """Function should raise ValueError on empty list."""
        with self.assertRaises(ValueError):
            mean_absolute_deviation([])


if __name__ == '__main__':
    unittest.main()
