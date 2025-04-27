import unittest
import decimal
# Assuming the code generated previously is saved in a file named 'rounding_logic.py'
# If not, replace 'rounding_logic' with the actual filename or paste the function here.
from generated_code import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_integer_string(self):
        """Test with a string representing a whole number."""
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("-5"), -5)
        self.assertEqual(closest_integer("0"), 0)

    def test_round_down(self):
        """Test rounding down for positive and negative numbers."""
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("-15.3"), -15)
        self.assertEqual(closest_integer("0.2"), 0)
        self.assertEqual(closest_integer("-0.2"), 0)

    def test_round_half_away_from_zero(self):
        """Test rounding .5 cases away from zero."""
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("-14.5"), -15)
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("-0.5"), -1)

    def test_round_up(self):
        """Test rounding up for positive and negative numbers."""
        self.assertEqual(closest_integer("15.7"), 16)
        self.assertEqual(closest_integer("-15.7"), -16)
        self.assertEqual(closest_integer("0.9"), 1)
        self.assertEqual(closest_integer("-0.9"), -1)

    def test_invalid_input(self):
        """Test that invalid number strings raise ValueError."""
        with self.assertRaises(ValueError):
            closest_integer("abc")
        with self.assertRaises(ValueError):
            closest_integer("1.2.3")
        with self.assertRaises(ValueError):
            closest_integer("")
        with self.assertRaises(ValueError):
            closest_integer(" 15 ") # Contains spaces, Decimal might handle, let's check


# To run the tests from the command line:
# python -m unittest your_test_file_name.py
# Or, if running within an IDE, use its test runner.

if __name__ == "__main__":
    # This allows running the tests directly by executing the script
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
