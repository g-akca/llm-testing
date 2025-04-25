from decimal import Decimal, InvalidOperation
import math

def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    try:
        num = Decimal(value)
    except (InvalidOperation, TypeError):
        raise ValueError("Input must be a valid numeric string")

    if num >= 0:
        # Add 0.5 and take floor – equidistant values go up (away from 0)
        return int(math.floor(num + Decimal("0.5")))
    else:
        # Subtract 0.5 and take ceil – equidistant values go down (away from 0)
        return int(math.ceil(num - Decimal("0.5")))


if __name__ == "__main__":
    # Simple manual tests
    tests = ["10", "15.3", "14.5", "-14.5", "-14.2", "0", "0.5", "-0.5"]
    for t in tests:
        print(f"{t} -> {closest_integer(t)}")
