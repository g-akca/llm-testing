def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    balance = 0
    for ch in brackets:
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1
            if balance < 0:  # More closing than opening
                return False
        else:
            # If any other character appears, it's invalid input
            raise ValueError("Input string contains characters other than '(' and ')'")
    return balance == 0
