import sys
from typing import List

# Check if Python version is 3.7 or higher for type hinting support if needed,
# although this specific code works fine in earlier 3.x versions too.
# This check is more illustrative for complex scenarios.
if sys.version_info < (3, 7):
    # Simple print for environments where logging might not be set up
    print("Warning: This code uses features best supported by Python 3.7+", file=sys.stderr)


def by_length(arr: List[int]) -> List[str]:
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]
            -> filter valid numbers -> [2, 1, 1, 4, 5, 8, 2, 3]
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8]
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

      If the array is empty, return an empty array:
      arr = []
      return []

      If the array has any strange number ignore it:
      arr = [1, -1 , 55]
            -> filter valid numbers -> [1]
            -> sort arr -> [1]
            -> reverse arr -> [1]
      return = ['One']
    """
    if not arr:
        return []

    # Dictionary mapping numbers 1-9 to their English names
    num_to_name = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }

    # 1. Filter the array to keep only integers between 1 and 9
    filtered_arr = [num for num in arr if isinstance(num, int) and 1 <= num <= 9]

    # If no valid numbers are found after filtering, return empty list
    if not filtered_arr:
        return []

    # 2. Sort the filtered array in ascending order
    filtered_arr.sort()

    # 3. Reverse the sorted array
    filtered_arr.reverse()

    # 4. Replace each number with its corresponding name
    result = [num_to_name[num] for num in filtered_arr]

    return result


# Example Usage (optional, for testing)
if __name__ == "__main__":
    arr1 = [2, 1, 1, 4, 5, 8, 2, 3]
    print(f"Input: {arr1}")
    print(f"Output: {by_length(arr1)}")
    # Expected: ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']

    arr2 = []
    print(f"Input: {arr2}")
    print(f"Output: {by_length(arr2)}")
    # Expected: []

    arr3 = [1, -1, 55]
    print(f"Input: {arr3}")
    print(f"Output: {by_length(arr3)}")
    # Expected: ['One']

    arr4 = [10, 0, -5, 100]
    print(f"Input: {arr4}")
    print(f"Output: {by_length(arr4)}")
    # Expected: []

    arr5 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Input: {arr5}")
    print(f"Output: {by_length(arr5)}")
    # Expected: ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
