from typing import List, Tuple, Set

def _neighbors(pos: Tuple[int, int], n: int) -> List[Tuple[int, int]]:
    """Return all in-bounds 4-connected neighbors of a grid cell."""
    (r, c) = pos
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            yield nr, nc

def minPath(grid: List[List[int]], k: int) -> List[int]:
    """
    Find the lexicographically minimum path of length ``k`` on the given grid.
    
    A *path of length k* is a sequence of exactly k (not necessarily distinct)
    cells, where consecutive cells share a side (4-connected movement).  Among
    all such paths we return the one whose list of visited values is
    lexicographically smallest.  It is guaranteed to be unique.
    
    Parameters
    ----------
    grid : 2-D list of int
        Square N×N grid containing every integer 1 … N² exactly once.
    k : int
        Desired length of the path (k ≥ 1).
    
    Returns
    -------
    List[int]
        The ordered list of grid values along the minimum path.
    """
    if k <= 0:
        raise ValueError("k must be positive")

    n = len(grid)
    # Locate the global minimum value (always 1 by the problem statement).
    min_val = float('inf')
    start: Tuple[int, int] = (-1, -1)
    for r in range(n):
        for c in range(n):
            if grid[r][c] < min_val:
                min_val = grid[r][c]
                start = (r, c)

    path = [min_val]
    frontier: Set[Tuple[int, int]] = {start}

    for _ in range(k - 1):
        next_cells_by_value = {}
        # Collect all reachable neighbors grouped by their grid value.
        for cell in frontier:
            for nb in _neighbors(cell, n):
                v = grid[nb[0]][nb[1]]
                if v not in next_cells_by_value:
                    next_cells_by_value[v] = set()
                next_cells_by_value[v].add(nb)

        # Pick the smallest value available for the next step.
        best_val = min(next_cells_by_value.keys())
        frontier = next_cells_by_value[best_val]
        path.append(best_val)

    return path


if __name__ == "__main__":
    # Example usage
    g1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    print(minPath(g1, 3))  # → [1, 2, 1]

    g2 = [[5, 9, 3],
          [4, 1, 6],
          [7, 8, 2]]
    print(minPath(g2, 1))  # → [1]
