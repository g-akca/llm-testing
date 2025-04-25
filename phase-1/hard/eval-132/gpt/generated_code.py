def is_nested(string: str) -> bool:
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True *iff* there exists a **balanced** subsequence
    whose nesting depth is at least 2 (i.e., some bracket pair is inside another).

    Examples
    --------
    >>> is_nested('[[]]')
    True
    >>> is_nested('[]]]]]]][[[[[]')
    False
    >>> is_nested('[][]')
    False
    >>> is_nested('[]')
    False
    >>> is_nested('[[][]]')
    True
    >>> is_nested('[[]][[')
    True
    """
    depth = 0           # current depth while scanning
    max_depth = 0       # deepest level reached within current balanced segment

    for ch in string:
        if ch == '[':
            depth += 1
            max_depth = max(max_depth, depth)
        elif ch == ']':
            if depth > 0:
                depth -= 1
                # When depth returns to zero we've closed a balanced segment.
                if depth == 0:
                    if max_depth >= 2:     # nested pair found in this segment
                        return True
                    max_depth = 0          # reset for the next segment
            else:
                # Stray closing bracket: reset the scan state
                depth = 0
                max_depth = 0

    return False
