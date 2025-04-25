import math
import os
import random
import re
import sys

def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    n = len(arr)
    # Iterate backwards from the last element down to the second element (index 1)
    # This way, the first index we find satisfying the condition will be the largest
    for i in range(n - 1, 0, -1):
        # Check if the element at index i is less than the element at index i-1
        if arr[i] < arr[i - 1]:
            # If the condition is met, return the current index i
            return i
    # If the loop completes without finding such an element, it means the array
    # is sorted in non-decreasing order (or has 0 or 1 elements).
    return -1

