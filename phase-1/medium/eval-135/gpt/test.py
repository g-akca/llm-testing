import unittest
from generated_code import can_arrange

class TestCanArrange(unittest.TestCase):

    def test_strictly_increasing(self):
        """Array is already in increasing order → should return -1."""
        self.assertEqual(can_arrange([1, 2, 3, 4, 5]), -1)

    def test_single_violation_middle(self):
        """Single drop in the middle of the array."""
        self.assertEqual(can_arrange([1, 2, 4, 3, 5]), 3)

    def test_violation_at_end(self):
        """Drop occurs at the last position."""
        self.assertEqual(can_arrange([10, 20, 30, 25]), 3)

    def test_violation_near_start(self):
        """Drop occurs right after the first element."""
        self.assertEqual(can_arrange([3, 1, 2, 4]), 1)


if __name__ == "__main__":
    unittest.main()
