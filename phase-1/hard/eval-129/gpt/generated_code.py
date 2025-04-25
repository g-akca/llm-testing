from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    """
    Given an N × N grid (N ≥ 2) that contains every integer from 1 to N × N
    exactly once, return the lexicographically-minimum path of length *k*
    obtainable by moving between edge-sharing neighbouring cells.

    A *path* of length *k* is a sequence of *k* cell visits
    (cells may repeat).  Among all valid paths, we compare the
    lists of cell-values lexicographically.  Because the value 1 is the
    global minimum and can always start a path (you may revisit cells
    and the grid has at least one neighbour in every position), the
    optimal path must start on the cell containing 1.  After that, to
    keep the sequence lexicographically minimal, at every step we move
    to the neighbour with the smallest value.

    The answer is guaranteed to be unique.

    Parameters
    ----------
    grid : List[List[int]]
        Square grid of distinct integers 1 … N².
    k : int
        Desired path length (k ≥ 1).

    Returns
    -------
    List[int]
        The ordered list of values along the minimum path.

    Examples
    --------
    >>> minPath([[1, 2, 3],
    ...          [4, 5, 6],
    ...          [7, 8, 9]], 3)
    [1, 2, 1]

    >>> minPath([[5, 9, 3],
    ...          [4, 1, 6],
    ...          [7, 8, 2]], 1)
    [1]
    """
    if k <= 0:
        raise ValueError("k must be a positive integer")

    n = len(grid)
    if n == 0 or any(len(row) != n for row in grid):
        raise ValueError("grid must be a non-empty square matrix")

    # Locate the unique cell that holds value 1
    start = None
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                start = (r, c)
                break
        if start:
            break

    if start is None:  # Should never happen with valid input
        raise ValueError("grid does not contain value 1")

    path = [1]
    r, c = start
    # 4-neighbour (Manhattan) moves
    neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for _ in range(1, k):
        best_val = float('inf')
        best_pos = None

        # Examine the up / down / left / right neighbours
        for dr, dc in neighbours:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                v = grid[nr][nc]
                if v < best_val:
                    best_val, best_pos = v, (nr, nc)

        # The grid is at least 2 × 2, so every cell has ≥ 2 neighbours;
        # best_pos will always be found.
        r, c = best_pos
        path.append(best_val)

    return path
