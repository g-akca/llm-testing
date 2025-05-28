from typing import List, Union


def split_words(txt: str) -> Union[List[str], int]:
    '''
    Given a string of words, return a list of words split on whitespace.
    If no whitespace exists in the text, split on commas ",".
    If no commas exist, return the number of lower-case letters whose position
    in the alphabet is odd (where `a` → 0, `b` → 1, …, `z` → 25).

    Examples
    --------
    >>> split_words("Hello world!")
    ['Hello', 'world!']
    >>> split_words("Hello,world!")
    ['Hello', 'world!']
    >>> split_words("abcdef")
    3
    '''
    # Case 1 – text contains any whitespace → split on runs of whitespace
    if any(ch.isspace() for ch in txt):
        return txt.split()

    # Case 2 – no whitespace but at least one comma → split on commas
    if ',' in txt:
        return txt.split(',')

    # Case 3 – no whitespace or commas → count odd-index lower-case letters
    odd_lower_count = 0
    for ch in txt:
        if 'a' <= ch <= 'z' and ((ord(ch) - ord('a')) & 1):
            odd_lower_count += 1
    return odd_lower_count
