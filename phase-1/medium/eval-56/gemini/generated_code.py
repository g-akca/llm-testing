import sys

# Check if the Python version is 3.7 or higher
if sys.version_info < (3, 7):
    print("This script requires Python 3.7 or higher.")
    sys.exit(1)


def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    >>> correct_bracketing("")
    True
    >>> correct_bracketing("<<<")
    False
    >>> correct_bracketing(">>>")
    False
    """
    depth = 0
    for bracket in brackets:
        if bracket == '<':
            depth += 1
        elif bracket == '>':
            if depth == 0:
                return False  # Closing bracket without a matching opening one
            depth -= 1
        # Assuming the input string only contains '<' and '>' as per the docstring
        # else:
        #     # Handle unexpected characters if necessary
        #     pass 

    # If depth is 0 at the end, all brackets were matched correctly
    return depth == 0


# Example of running doctests (optional, but good practice)
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Additional manual tests
    print(f"'<': {correct_bracketing('<')}")
    print(f"'<>': {correct_bracketing('<>')}")
    print(f"'<<><>>': {correct_bracketing('<<><>>')}")
    print(f"'>><<': {correct_bracketing('><<>')}")
    print(f"Empty string '': {correct_bracketing('')}")
    print(f"'<<<': {correct_bracketing('<<<')}")
    print(f"'>>>': {correct_bracketing('>>>')}")
    print(f"'<><>': {correct_bracketing('<><>')}")
    print(f"'<<>>': {correct_bracketing('<<>>')}")
