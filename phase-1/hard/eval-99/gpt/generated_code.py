import math
from decimal import Decimal, InvalidOperation, ROUND_FLOOR, ROUND_CEILING

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
    # --- Parse the input safely using Decimal for accuracy ---
    try:
        num = Decimal(value)
    except (InvalidOperation, TypeError):
        raise ValueError("Input must be a string representation of a numeric value")

    # If already an integer, return it quickly
    if num == int(num):
        return int(num)

    # Determine sign once (0 treated as positive for rounding logic)
    sign = 1 if num >= 0 else -1

    # Absolute distance to the nearest lower integer
    fractional_part = abs(num - int(num))

    # Exactly halfway (.5) → need to move away from zero
    if fractional_part == Decimal("0.5"):
        return int(num.to_integral_exact(rounding=ROUND_CEILING if sign == 1 else ROUND_FLOOR))

    # Otherwise, use normal rounding to the nearest integer
    # Decimal's quantize makes behavior explicit and consistent
    nearest = num.to_integral_value(rounding=ROUND_FLOOR if fractional_part < Decimal("0.5") else ROUND_CEILING)
    return int(nearest)
