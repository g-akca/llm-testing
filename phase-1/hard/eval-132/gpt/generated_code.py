def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') → True
    is_nested('[]]]]]]][[[[[]') → False
    is_nested('[][]') → False
    is_nested('[]') → False
    is_nested('[[][]]') → True
    is_nested('[[]][[') → True
    '''
    max_depth = 0      # deepest level reached by any valid bracket pair
    current_depth = 0  # current level while scanning
    for ch in string:
        if ch == '[':
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        elif ch == ']':
            # only pop if there is a matching '['
            if current_depth > 0:
                current_depth -= 1
    # A nested subsequence exists iff the maximum depth reached was ≥ 2
    return max_depth >= 2


if __name__ == "__main__":
    # basic sanity checks from the examples
    tests = {
        "[[]]": True,
        "[]]]]]]][[[[[]": False,
        "[][]": False,
        "[]": False,
        "[[][]]": True,
        "[[]][[": True,
    }

    for s, expected in tests.items():
        result = is_nested(s)
        print(f"is_nested({s!r}) = {result}  (expected {expected})")
