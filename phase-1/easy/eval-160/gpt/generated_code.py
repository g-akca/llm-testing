from typing import List


def do_algebra(operator: List[str], operand: List[int]) -> int:
    """
    Build an algebraic expression from two parallel lists—one of operators and
    one of operands—and return its evaluated result.

    Parameters
    ----------
    operator : List[str]
        A list whose elements are strings representing basic algebra operators:
        '+', '-', '*', '//', or '**'.
    operand : List[int]
        A list of non-negative integers (length must be exactly one greater
        than the operator list).

    Returns
    -------
    int
        The integer result of evaluating the constructed expression.

    Examples
    --------
    >>> do_algebra(['+', '*', '-'], [2, 3, 4, 5])
    9
    >>> do_algebra(['**', '+'], [2, 3, 1])
    9  # 2 ** 3 + 1
    """
    # Basic validation of list lengths and operator set
    if len(operator) != len(operand) - 1:
        raise ValueError("operator must be exactly one element shorter than operand")
    allowed_ops = {"+", "-", "*", "//", "**"}
    if any(op not in allowed_ops for op in operator):
        raise ValueError("Unsupported operator encountered")

    # Efficiently build the expression as a string, then evaluate it
    expr_parts = [str(operand[0])]
    for op, num in zip(operator, operand[1:]):
        expr_parts.append(op)
        expr_parts.append(str(num))
    expression = " ".join(expr_parts)

    # Safe enough here because operands are numbers and operators are validated
    return int(eval(expression))


if __name__ == "__main__":
    # Simple demo
    print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # -> 9
