import sys
from typing import Tuple

# Make sure we are using Python 3.7 or higher for type hinting support
# Although the core logic works in earlier Python 3 versions.
if sys.version_info < (3, 7):
    print(
        "Warning: This code uses type hints available in Python 3.7+",
        file=sys.stderr,
    )


def is_palindrome(num: int) -> bool:
    """Helper function to check if a number is a palindrome."""
    # Single digit numbers are always palindromes
    if num < 0:
        return False  # Negative numbers are not considered palindromes here
    if num < 10:
        return True
    return str(num) == str(num)[::-1]


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input n must be a positive integer.")
    # Constraint check (optional but good practice)
    if n > 1000:
        print(
            "Warning: Input n exceeds the specified constraint of 1000.",
            file=sys.stderr,
        )

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_palindrome_count += 1
            else:
                odd_palindrome_count += 1

    return (even_palindrome_count, odd_palindrome_count)


# Example Usage (optional, for testing)
if __name__ == "__main__":
    print(f"Input: 3, Output: {even_odd_palindrome(3)}")
    print(f"Input: 12, Output: {even_odd_palindrome(12)}")
    print(f"Input: 100, Output: {even_odd_palindrome(100)}")
    # Palindromes up to 100: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99
    # Even: 2, 4, 6, 8, 22, 44, 66, 88 (8)
    # Odd: 1, 3, 5, 7, 9, 11, 33, 55, 77, 99 (10)
    # Expected: (8, 10)
