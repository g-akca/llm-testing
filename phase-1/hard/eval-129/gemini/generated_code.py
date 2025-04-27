import math

def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    N = len(grid)
    
    # Since we want the lexicographically smallest path, the path must start
    # with the smallest possible value, which is 1.
    # Find the coordinates of the cell with value 1.
    start_r, start_c = -1, -1
    pos_map = {} # Optional: map value to position for faster lookup if needed later
    for r in range(N):
        for c in range(N):
            val = grid[r][c]
            pos_map[val] = (r, c)
            if val == 1:
                start_r, start_c = r, c
                # No need to break early if building pos_map
    
    # If k is 1, the path is just the starting cell's value
    if k == 1:
        return [1]

    # Initialize the path and current position
    current_r, current_c = start_r, start_c
    min_path_values = [grid[current_r][current_c]] # Starts with [1]

    # Define possible moves (up, down, left, right)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Build the path greedily for k-1 steps
    for _ in range(k - 1):
        min_neighbor_val = float('inf')
        next_r, next_c = -1, -1

        # Check all valid neighbors
        for dr, dc in moves:
            nr, nc = current_r + dr, current_c + dc

            # Check if the neighbor is within the grid boundaries
            if 0 <= nr < N and 0 <= nc < N:
                neighbor_val = grid[nr][nc]
                # If this neighbor has a smaller value, it's our current best choice
                if neighbor_val < min_neighbor_val:
                    min_neighbor_val = neighbor_val
                    next_r, next_c = nr, nc
        
        # Move to the neighbor with the minimum value
        current_r, current_c = next_r, next_c
        min_path_values.append(grid[current_r][current_c])

    return min_path_values

