import sys
from typing import List

# Ensure compatibility with Python 3.7
if sys.version_info < (3, 7):
    print("This script requires Python 3.7 or later.")
    sys.exit(1)


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    >>> separate_paren_groups('()')
    ['()']
    >>> separate_paren_groups('(())')
    ['(())']
    >>> separate_paren_groups('()()()')
    ['()', '()', '()']
    >>> separate_paren_groups('(()()) ((())) ()')
    ['(()())', '((()))', '()']
    >>> separate_paren_groups('')
    []
    >>> separate_paren_groups('   ')
    []
    >>> separate_paren_groups(' ( ) ')
    ['()']
    """
    result: List[str] = []
    current_group_chars: List[str] = []
    depth = 0

    for char in paren_string:
        if char == ' ':
            continue  # Ignore spaces

        if char == '(':
            depth += 1
            current_group_chars.append(char)
        elif char == ')':
            # Only process closing parenthesis if we are inside a group
            if depth > 0:
                current_group_chars.append(char)
                depth -= 1
                # If depth becomes 0, we have closed a top-level group
                if depth == 0:
                    result.append("".join(current_group_chars))
                    current_group_chars = []  # Reset for the next group
        # If depth > 0 and char is neither '(' nor ')', it would be appended here
        # but the problem description implies only parentheses and spaces.
        # If other characters were allowed inside, we'd need:
        # elif depth > 0:
        #     current_group_chars.append(char)

    # Note: If the input string has unbalanced parentheses (e.g., "(()"),
    # the partially formed group in current_group_chars will be discarded
    # because depth will not return to 0 at the end. This matches the
    # requirement of returning only balanced groups.

    return result


# Example usage (optional, as doctests cover examples)
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(separate_paren_groups('( ) (( )) (( )( ))'))
    print(separate_paren_groups('()()()'))
    print(separate_paren_groups('(()()) ((())) ()'))
    print(separate_paren_groups(''))
    print(separate_paren_groups(' ( ) '))
