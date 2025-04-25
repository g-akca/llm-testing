import unittest
from typing import List
from generated_code import unique


class TestUniqueFunction(unittest.TestCase):

    def test_basic_case_with_duplicates(self):
        """Tests a typical list with duplicates and unsorted elements."""
        self.assertEqual(
            unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123]
        )

    def test_empty_list(self):
        """Tests if the function handles an empty list correctly."""
        self.assertEqual(unique([]), [])

    def test_list_with_no_duplicates(self):
        """Tests a list that already contains unique, unsorted elements."""
        self.assertEqual(unique([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])

    def test_list_with_all_duplicates(self):
        """Tests a list where all elements are the same."""
        self.assertEqual(unique([7, 7, 7, 7, 7]), [7])

    def test_list_already_sorted_unique(self):
        """Tests a list that is already sorted and unique."""
        self.assertEqual(unique([10, 20, 30, 40]), [10, 20, 30, 40])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
