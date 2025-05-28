from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string representing multiple groups of nested
    parentheses separated by spaces. For each group, return the deepest level
    of nesting.

    A single pair "()" has depth 1.  
    For example:
        - "(()())"  → depth 2  
        - "((()))"  → depth 3

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depths: List[int] = []

    # Split on any amount of whitespace; ignore empty chunks
    for group in paren_string.strip().split():
        max_depth = 0
        current_depth = 0

        for ch in group:
            if ch == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif ch == ')':
                # Assume input groups are balanced; otherwise this would go negative
                current_depth -= 1

        depths.append(max_depth)

    return depths
