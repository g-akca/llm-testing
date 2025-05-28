from typing import List

def move_one_ball(arr: List[int]) -> bool:
    """
    We have an array `arr` of N unique integers.  You are allowed to perform a *right-shift*
    (rotate right) any number of times.  A right-shift moves every element one position to
    the right and places the last element at index 0.

    Return **True** if the array can be transformed into non-decreasing order by some
    (possibly zero) number of right-shifts, and **False** otherwise.
    An empty array is considered already sorted → return **True**.

    Example
    -------
    >>> move_one_ball([3, 4, 5, 1, 2])
    True        # two right-shifts give [1, 2, 3, 4, 5]

    >>> move_one_ball([3, 5, 4, 1, 2])
    False       # no rotation yields a sorted array
    """
    n = len(arr)
    if n == 0:
        return True

    # Count how many times the ascending order "drops" when moving left-to-right,
    # wrapping around at the end.
    drops = 0
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            drops += 1
            if drops > 1:          # More than one drop => cannot be a sorted rotation
                return False

    return True  # Zero or one drop means a rotation produces sorted order


if __name__ == "__main__":
    # Simple sanity checks
    assert move_one_ball([]) is True
    assert move_one_ball([1]) is True
    assert move_one_ball([3, 4, 5, 1, 2]) is True
    assert move_one_ball([3, 5, 4, 1, 2]) is False
    print("All tests passed.")
