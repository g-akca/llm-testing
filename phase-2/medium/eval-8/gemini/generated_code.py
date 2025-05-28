from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_val = 0
    prod_val = 1

    for num in numbers:
        sum_val += num
        prod_val *= num

    return (sum_val, prod_val)
