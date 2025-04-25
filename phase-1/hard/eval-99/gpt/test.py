import unittest
from decimal import Decimal
# Import the function from the module where it is defined.
# If the function is in a file named `closest.py`, you would do:
from generated_code import closest_integer
# For this example, we assume the function is available in the same namespace.

class TestClosestInteger(unittest.TestCase):
    def test_positive_integer(self):
        """Exact integer should return itself."""
        self.assertEqual(closest_integer("10"), 10)

    def test_positive_decimal_round_down(self):
        """Non-half positive decimal should round toward the nearest lower integer."""
        self.assertEqual(closest_integer("15.3"), 15)

    def test_positive_half_round_away(self):
        """Positive .5 value should round away from zero (up)."""
        self.assertEqual(closest_integer("14.5"), 15)

    def test_negative_half_round_away(self):
        """Negative -.5 value should round away from zero (down)."""
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_invalid_input_raises(self):
        """Non-numeric strings should raise ValueError."""
        with self.assertRaises(ValueError):
            closest_integer("not_a_number")

if __name__ == "__main__":
    unittest.main()
