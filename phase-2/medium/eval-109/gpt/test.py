import unittest

# Adjust the import below to match where `move_one_ball` lives.
# If the function is in `move_one_ball.py`, leave as-is; otherwise change accordingly.
from generated_code import move_one_ball  


class MoveOneBallTests(unittest.TestCase):
    def test_empty_array(self):
        """An empty list is considered sorted."""
        self.assertTrue(move_one_ball([]))

    def test_single_element(self):
        """A single element is already sorted."""
        self.assertTrue(move_one_ball([42]))

    def test_rotation_succeeds(self):
        """Array that becomes sorted after two right shifts."""
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))

    def test_already_sorted(self):
        """Array already in non-decreasing order needs zero shifts."""
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_rotation_fails(self):
        """Array with more than one descending 'drop' cannot be sorted via rotation."""
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))


if __name__ == "__main__":
    unittest.main()
