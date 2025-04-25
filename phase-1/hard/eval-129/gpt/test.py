import unittest
from itertools import product
from typing import List, Tuple
from generated_code import minPath, _neighbors

class TestMinPath(unittest.TestCase):
    def test_example_three_by_three(self):
        grid = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
        self.assertEqual(minPath(grid, 3), [1, 2, 1])

    def test_example_single_step(self):
        grid = [[5, 9, 3],
                [4, 1, 6],
                [7, 8, 2]]
        self.assertEqual(minPath(grid, 1), [1])

    def test_correct_length(self):
        grid = [[1, 2],
                [3, 4]]
        k = 5
        result = minPath(grid, k)
        self.assertEqual(len(result), k,
                         msg="Returned path should contain exactly k values")

    def test_matches_bruteforce_for_small_grid(self):
        """
        For a 2×2 grid and small k we can exhaustively enumerate every
        possible path and verify that minPath returns the lexicographically
        minimal one.
        """
        grid = [[2, 3],
                [4, 1]]  # '1' is at (1,1)
        n = len(grid)
        k = 4

        def brute_force() -> List[int]:
            # Pre-compute coordinates for convenience
            coords = [(r, c) for r, c in product(range(n), repeat=2)]

            best = None
            for start in coords:
                stack = [(start, [grid[start[0]][start[1]]])]
                while stack:
                    (r, c), path = stack.pop()
                    if len(path) == k:
                        if best is None or path < best:
                            best = path
                        continue
                    for nr, nc in _neighbors((r, c), n):
                        stack.append(((nr, nc),
                                      path + [grid[nr][nc]]))
            return best

        self.assertEqual(minPath(grid, k), brute_force())


if __name__ == "__main__":
    unittest.main()
