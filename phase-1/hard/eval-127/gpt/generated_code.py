import math
from typing import Tuple

def _is_prime(n: int) -> bool:
    """Return True if `n` is a prime number, else False."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    """
    Determine whether the length of the intersection of two closed intervals
    is a prime number.

    Parameters
    ----------
    interval1 : Tuple[int, int]
        First closed interval (start, end), start <= end.
    interval2 : Tuple[int, int]
        Second closed interval (start, end), start <= end.

    Returns
    -------
    str
        "YES" if the length of the intersection is a prime number,
        otherwise "NO". If the intervals do not intersect, returns "NO".
    """
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    # No intersection if the calculated start is greater than end
    if start > end:
        return "NO"

    length = end - start  # Closed intervals: length measured as end - start

    return "YES" if _is_prime(length) else "NO"
