def _is_prime(n: int) -> bool:
    """Return True if *n* is a prime number (> 1)."""
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    step = 2  # alternates 2, 4 to test 6k±1 numbers
    while i * i <= n:
        if n % i == 0:
            return False
        i += step
        step = 6 - step  # switch between +2 and +4
    return True


def intersection(interval1, interval2):
    """
    Determine whether the (non-negative) length of the intersection of two closed
    integer intervals is a prime number.

    Each interval is a 2-tuple (start, end) with start ≤ end.  
    The length is defined as end − start for the intersecting part.

    Returns
    -------
    "YES" if the length is prime, otherwise "NO".
    """
    a1, b1 = interval1
    a2, b2 = interval2

    # Calculate the intersection’s bounds
    start = max(a1, a2)
    end = min(b1, b2)

    # No intersection or a single-point intersection → length 0
    if start >= end:
        return "NO"

    length = end - start
    return "YES" if _is_prime(length) else "NO"
