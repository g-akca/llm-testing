from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Split a string that contains several *disjoint*-but-possibly-nested groups
    of parentheses into a list of the individual, balanced groups.

    - Groups are **not** nested inside each other; once a group starts,
      it runs to completion before the next one begins.
    - Any space characters should be ignored.

    Examples
    --------
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()()))']

    >>> separate_paren_groups('(()()) ()')
    ['(()())', '()']

    Parameters
    ----------
    paren_string : str
        A string consisting only of `'('`, `')'`, and (optional) spaces.

    Returns
    -------
    List[str]
        Each element is one balanced, complete parenthesis group.
    """
    groups: List[str] = []           # Final list of completed groups
    current: List[str] = []          # Characters for the group in progress
    depth: int = 0                   # Current parenthesis nesting depth

    for ch in paren_string:
        if ch == ' ':                # Skip spaces entirely
            continue

        if ch not in '()':
            raise ValueError(f"Invalid character {ch!r} in input; "
                             "only spaces and parentheses are allowed")

        # Always append the parenthesis character we just saw
        current.append(ch)

        # Update nesting depth
        depth += 1 if ch == '(' else -1

        # When depth returns to zero, we just closed a complete group
        if depth == 0:
            groups.append(''.join(current))
            current.clear()          # Start fresh for the next group

        # `depth` should never be negative for a well-formed input
        if depth < 0:
            raise ValueError("Unbalanced parentheses: too many ')' characters")

    if depth != 0:
        raise ValueError("Unbalanced parentheses: unfinished '(' group")

    return groups


# --- Minimal self-test / demo ---------------------------------------------
if __name__ == "__main__":
    sample = "( ) (( )) (( )( ))"
    print("Input :", sample)
    print("Output:", separate_paren_groups(sample))
