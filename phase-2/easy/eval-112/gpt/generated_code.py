from typing import Tuple

def reverse_delete(s: str, c: str) -> Tuple[str, bool]:
    """
    Task
    We are given two strings `s` and `c`.  Delete every character from `s`
    that also appears in `c`, then check whether the resulting string is
    a palindrome.

    A string is a palindrome if it reads the same backward as forward.

    Return
    -------
    Tuple[str, bool]
        A tuple containing the filtered string and `True` if it is a
        palindrome, `False` otherwise.

    Examples
    --------
    >>> reverse_delete("abcde", "ae")
    ('bcd', False)
    >>> reverse_delete("abcdef", "b")
    ('acdef', False)
    >>> reverse_delete("abcdedcba", "ab")
    ('cdedc', True)
    """
    remove_chars = set(c)                       # characters to delete
    filtered = ''.join(ch for ch in s if ch not in remove_chars)
    is_pal = filtered == filtered[::-1]         # palindrome check
    return filtered, is_pal
