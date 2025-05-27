import math

def is_prime(n):
    """Checks if a non-negative integer n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check odd divisors up to the square root of n
    # Use int(math.sqrt(n)) for Python 3.7 compatibility
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
    s1, e1 = interval1
    s2, e2 = interval2

    # Find the potential intersection interval
    # The start of the intersection is the maximum of the starts
    # The end of the intersection is the minimum of the ends
    intersect_start = max(s1, s2)
    intersect_end = min(e1, e2)

    # Check if the intervals actually intersect
    # Intersection exists only if start <= end
    if intersect_start > intersect_end:
        return "NO"  # No intersection

    # Calculate the length of the intersection
    # Length = end - start (for a closed interval)
    length = intersect_end - intersect_start

    # Check if the length is a prime number
    if is_prime(length):
        return "YES"
    else:
        return "NO"

# Example Usage (from prompt):
# print(f"intersection((1, 2), (2, 3)) ==> \"{intersection((1, 2), (2, 3))}\"")
# print(f"intersection((-1, 1), (0, 4)) ==> \"{intersection((-1, 1), (0, 4))}\"")
# print(f"intersection((-3, -1), (-5, 5)) ==> \"{intersection((-3, -1), (-5, 5))}\"")
# print(f"intersection((1, 3), (2, 4)) ==> \"{intersection((1, 3), (2, 4))}\"") # Example from description
# print(f"intersection((1, 5), (2, 6)) ==> \"{intersection((1, 5), (2, 6))}\"") # Intersection (2, 5), length 3 (prime) -> YES
# print(f"intersection((5, 6), (1, 4)) ==> \"{intersection((5, 6), (1, 4))}\"") # No intersection -> NO
