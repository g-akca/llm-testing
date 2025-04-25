from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove all whitespace characters
    cleaned = paren_string.replace(" ", "")

    groups: List[str] = []
    current: List[str] = []
    depth = 0

    for ch in cleaned:
        if ch not in "()":
            # Ignore anything that is not a parenthesis
            continue

        current.append(ch)

        # Update nesting depth
        if ch == "(":
            depth += 1
        else:  # ch == ")"
            depth -= 1

        # When depth returns to zero, we’ve closed a complete group
        if depth == 0:
            groups.append("".join(current))
            current = []  # start next group

    return groups


if __name__ == "__main__":
    # Simple sanity check
    sample = "( ) (( )) (( )( ))"
    print(separate_paren_groups(sample))  # ['()', '(())', '(()())']
