# vowels_count.py
# Python 3.7+

FIX = """
Add more test cases.
"""

def vowels_count(s: str) -> int:
    """
    Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'.  Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    s_lower = s.lower()
    core_vowels = {"a", "e", "i", "o", "u"}

    total = 0
    for idx, ch in enumerate(s_lower):
        if ch in core_vowels:
            total += 1
        elif ch == "y" and idx == len(s_lower) - 1:
            total += 1
    return total
