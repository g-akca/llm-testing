import unittest
from generated_code import closest_integer


class TestClosestInteger(unittest.TestCase):

    def test_exact_integer(self):
        """Should return the integer itself when the input is already integral."""
        self.assertEqual(closest_integer("10"), 10)

    def test_round_down(self):
        """Fractional part < 0.5 should round toward zero."""
        self.assertEqual(closest_integer("15.3"), 15)

    def test_round_up(self):
        """Fractional part > 0.5 should round away from zero."""
        self.assertEqual(closest_integer("-2.51"), -3)

    def test_half_away_from_zero_positive(self):
        """Exactly halfway for a positive number should round up (away from zero)."""
        self.assertEqual(closest_integer("14.5"), 15)

    def test_half_away_from_zero_negative(self):
        """Exactly halfway for a negative number should round down (away from zero)."""
        self.assertEqual(closest_integer("-14.5"), -15)


if __name__ == "__main__":
    unittest.main()
