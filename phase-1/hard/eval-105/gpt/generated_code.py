def by_length(arr):
    """
    Sort the input list, reverse it, and map digits 1–9 to their English names.

    Steps:
    1. Sort the entire list in ascending order.
    2. Reverse the sorted list (descending order).
    3. Keep only values in the range 1–9 (inclusive).
    4. Convert each remaining digit to its corresponding name.

    Examples
    --------
    >>> by_length([2, 1, 1, 4, 5, 8, 2, 3])
    ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']

    >>> by_length([])
    []

    >>> by_length([1, -1, 55])
    ['One']
    """
    digit_names = {
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

    # Step 1 & 2: sort ascending then reverse (descending)
    sorted_reversed = list(reversed(sorted(arr)))

    # Step 3 & 4: filter to 1–9 and map to names
    return [digit_names[num] for num in sorted_reversed if 1 <= num <= 9]
