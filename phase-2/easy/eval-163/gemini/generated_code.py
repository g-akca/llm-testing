import math

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower_bound = min(a, b)
    upper_bound = max(a, b)
    
    even_digits = [0, 2, 4, 6, 8]
    result = []
    
    for digit in even_digits:
        if lower_bound <= digit <= upper_bound:
            result.append(digit)
            
    # The result is already sorted because we iterate through even_digits in ascending order.
    return result

