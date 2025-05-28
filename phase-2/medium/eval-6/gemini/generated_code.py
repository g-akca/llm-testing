import sys
# Ensure compatibility with Python 3.7 by adding List from typing
if sys.version_info < (3, 9):
    from typing import List
else:
    from builtins import list as List

def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    >>> parse_nested_parens('')
    [0]
    >>> parse_nested_parens('()')
    [1]
    >>> parse_nested_parens('((()))')
    [3]
    >>> parse_nested_parens('() (()) ((())) (((())))')
    [1, 2, 3, 4]
    >>> parse_nested_parens('   ') # Test with multiple spaces
    [0, 0, 0, 0]
    """
    groups = paren_string.split(' ')
    result = []

    for group in groups:
        max_depth = 0
        current_depth = 0
        if not group: # Handle empty strings resulting from multiple spaces
            result.append(0)
            continue
            
        for char in group:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                # We only care about the max depth reached,
                # so decrementing is enough.
                # No need to check for negative depth for this problem.
                current_depth -= 1
        
        result.append(max_depth)

    return result

# Example of running the doctests if the script is executed directly
if __name__ == "__main__":
    import doctest
    doctest.testmod()

