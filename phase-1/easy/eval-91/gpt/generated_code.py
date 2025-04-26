import re
from typing import List

def is_bored(S: str) -> int:
    """
    Count how many sentences in *S* start with the word **I**.

    A sentence is any substring separated by '.', '?' or '!'.
    Leading/trailing whitespace around each sentence is ignored.
    The first word must be exactly "I" (uppercase, no punctuation).

    Examples
    --------
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    if not S:
        return 0

    # Split on '.', '?', or '!' and strip whitespace from each piece
    sentences: List[str] = [seg.strip() for seg in re.split(r"[.?!]", S)]

    # Count sentences where the very first word is "I"
    return sum(
        1
        for sentence in sentences
        if sentence and (sentence == "I" or sentence.startswith("I "))
    )
