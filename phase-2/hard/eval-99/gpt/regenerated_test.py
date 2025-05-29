import unittest
from regenerated_code import closest_integer

class TestClosestInteger(unittest.TestCase):
    def test_integer_input(self):
        self.assertEqual(closest_integer("10"), 10)

    def test_regular_rounding_down(self):
        self.assertEqual(closest_integer("15.3"), 15)

    def test_regular_rounding_up(self):
        self.assertEqual(closest_integer("15.7"), 16)

    def test_half_away_from_zero_positive(self):
        self.assertEqual(closest_integer("14.5"), 15)

    def test_half_away_from_zero_negative(self):
        self.assertEqual(closest_integer("-14.5"), -15)

if __name__ == "__main__":
    unittest.main()
