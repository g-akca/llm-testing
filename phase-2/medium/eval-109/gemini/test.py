import unittest
from generated_code import move_one_ball

class TestMoveOneBall(unittest.TestCase):

    def test_empty_list(self):
        """Test case for an empty list."""
        self.assertTrue(move_one_ball([]), "Empty list should return True")

    def test_single_element_list(self):
        """Test case for a list with a single element."""
        self.assertTrue(
            move_one_ball([5]), "Single element list should return True"
        )

    def test_already_sorted(self):
        """Test case for an already sorted list."""
        self.assertTrue(
            move_one_ball([1, 2, 3, 4, 5]),
            "Already sorted list should return True",
        )

    def test_sortable_by_rotation(self):
        """Test case for a list that can be sorted by rotation (example 1)."""
        self.assertTrue(
            move_one_ball([3, 4, 5, 1, 2]),
            "List [3, 4, 5, 1, 2] should be sortable by rotation",
        )

    def test_not_sortable_by_rotation(self):
        """Test case for a list that cannot be sorted by rotation (example 2)."""
        self.assertFalse(
            move_one_ball([3, 5, 4, 1, 2]),
            "List [3, 5, 4, 1, 2] should not be sortable by rotation",
        )

    def test_sortable_by_one_rotation(self):
        """Test case for a list sortable by a single rotation."""
        self.assertTrue(
            move_one_ball([5, 1, 2, 3, 4]),
            "List [5, 1, 2, 3, 4] should be sortable by rotation",
        )

    def test_not_sortable_simple(self):
        """Test case for a simple non-sortable list."""
        self.assertFalse(
            move_one_ball([1, 3, 2, 4]),
            "List [1, 3, 2, 4] should not be sortable by rotation",
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
