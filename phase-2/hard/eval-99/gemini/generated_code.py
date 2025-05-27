import decimal
import math

def closest_integer(value: str) -> int:
    """
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    >>> closest_integer("0")
    0
    >>> closest_integer("-0.5")
    -1


    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    """
    try:
        # Use Decimal for precise rounding control
        d_value = decimal.Decimal(value)
    except decimal.InvalidOperation:
        # Handle cases where the string is not a valid number
        raise ValueError(f"Input string '{value}' is not a valid number.")

    # ROUND_HALF_UP rounds .5 away from zero, exactly as required.
    # We quantize to the nearest integer (Decimal('1')).
    rounded_value = d_value.quantize(
        decimal.Decimal("1"), rounding=decimal.ROUND_HALF_UP
    )

    return int(rounded_value)

# Example Usage (from docstring):
print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))
print(closest_integer("0"))
print(closest_integer("-0.5"))

# Additional test cases
print(closest_integer("14.49"))
print(closest_integer("-14.49"))
print(closest_integer("14.51"))
print(closest_integer("-14.51"))
