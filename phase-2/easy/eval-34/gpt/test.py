import unittest
from generated_code import unique   # assumes the function is saved in `unique.py`


class TestUnique(unittest.TestCase):
    def test_example_from_docstring(self):
        self.assertEqual(
            unique([5, 3, 5, 2, 3, 3, 9, 0, 123]),
            [0, 2, 3, 5, 9, 123],
        )

    def test_already_unique_sorted(self):
        self.assertEqual(unique([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_all_duplicates(self):
        self.assertEqual(unique([7, 7, 7]), [7])

    def test_with_negative_and_zero(self):
        self.assertEqual(unique([-2, -1, 0, -2, 0]), [-2, -1, 0])


if __name__ == "__main__":
    unittest.main()
