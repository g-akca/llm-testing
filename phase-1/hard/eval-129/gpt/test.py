import unittest

from code import minPath   # replace with the actual module name


class TestMinPath(unittest.TestCase):
    def test_example_3x3_k3(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(minPath(grid, 3), [1, 2, 1])

    def test_example_3x3_k1(self):
        grid = [
            [5, 9, 3],
            [4, 1, 6],
            [7, 8, 2]
        ]
        self.assertEqual(minPath(grid, 1), [1])

    def test_2x2_revisiting_allowed(self):
        grid = [
            [1, 2],
            [3, 4]
        ]
        # Best lexicographic path of length 4 is 1 → 2 → 1 → 2
        self.assertEqual(minPath(grid, 4), [1, 2, 1, 2])

    def test_invalid_k_raises(self):
        grid = [
            [1, 2],
            [3, 4]
        ]
        with self.assertRaises(ValueError):
            minPath(grid, 0)


if __name__ == "__main__":
    unittest.main()
