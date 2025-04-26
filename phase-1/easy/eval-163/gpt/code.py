from typing import List


def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers ``a`` and ``b``, return a list containing all **even
    single-digit integers** (2, 4, 6, 8) that lie between ``a`` and ``b`` (inclusive),
    in ascending order.

    Examples
    --------
    >>> generate_integers(2, 8)
    [2, 4, 6, 8]
    >>> generate_integers(8, 2)
    [2, 4, 6, 8]
    >>> generate_integers(10, 14)
    []
    """
    # --- input validation ----------------------------------------------------
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Both a and b must be integers.")
    if a <= 0 or b <= 0:
        raise ValueError("Both a and b must be positive integers (> 0).")

    low, high = sorted((a, b))  # inclusive bounds, regardless of order
    even_digits = (2, 4, 6, 8)  # the only even single-digit integers

    # Filter and return those even digits that fall inside [low, high]
    return [d for d in even_digits if low <= d <= high]
