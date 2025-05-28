import doctest

FIX = """
Add more test cases.
"""


def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    >>> vowels_count("") # Test empty string
    0
    >>> vowels_count("rhythm") # Test no standard vowels, y not at end
    0
    >>> vowels_count("aeiou") # Test all standard vowels
    5
    >>> vowels_count("fly") # Test y at end as only vowel
    1
    >>> vowels_count("yellow") # Test y not at end
    2
    >>> vowels_count("Programming") # Test mixed case
    3
    >>> vowels_count("beauty") # Test y at end with other vowels
    4
    >>> vowels_count("y") # Test single character y
    1
    >>> vowels_count("Y") # Test single character Y
    1
    >>> vowels_count("PYTHONy") # Test mixed case with y at end
    2
    >>> vowels_count("syzygy") # Test multiple y's, only last counts
    1
    """
    vowels = "aeiou"
    count = 0
    s_lower = s.lower()  # Work with lowercase version for comparison

    # Count standard vowels
    for char in s_lower:
        if char in vowels:
            count += 1

    # Check if the string is not empty and the last character is 'y'
    if s and s_lower[-1] == "y":
        count += 1

    return count


# Optional: Run doctests when the script is executed
if __name__ == "__main__":
    doctest.testmod()
