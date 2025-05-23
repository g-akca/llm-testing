import collections
from typing import List

def move_one_ball(arr: List[int]) -> bool:
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """
    if not arr:
        return True

    n = len(arr)
    if n == 1:
        return True

    # Create the target sorted array
    sorted_arr = sorted(arr)

    # If the array can be sorted by rotation, the sorted version must exist
    # as one of the possible rotations of the original array.
    # We can check this efficiently by concatenating the original array
    # with itself and seeing if the sorted array exists as a sublist.

    doubled_arr = arr + arr

    # Check if sorted_arr is a contiguous sublist within doubled_arr
    # We only need to check starting positions from index 0 to n-1
    for i in range(n):
        # Extract a sublist of length n starting at index i
        sub_list = doubled_arr[i : i + n]
        # Compare with the sorted array
        if sub_list == sorted_arr:
            return True

    # If no rotation matches the sorted array after checking all possibilities
    return False

