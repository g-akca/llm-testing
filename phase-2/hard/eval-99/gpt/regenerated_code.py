from decimal import Decimal

def closest_integer(value):
    """
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
    """
    d = Decimal(value)
    # fractional part in [0, 1)
    frac = abs(d % 1)
    # special case: exactly .5 fraction — round away from zero
    if frac == Decimal("0.5"):
        sign = 1 if d >= 0 else -1
        magnitude = int(abs(d))
        return sign * (magnitude + 1)
    # all other cases: use Python's built-in round (banker's rounding)
    return round(float(d))
