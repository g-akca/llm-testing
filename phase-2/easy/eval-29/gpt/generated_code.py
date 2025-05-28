from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix.

    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    # Guard clause: if the prefix is empty, return the original list unchanged
    if prefix == "":
        return list(strings)

    # Use a list comprehension to keep only strings that start with the given prefix
    return [s for s in strings if isinstance(s, str) and s.startswith(prefix)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
