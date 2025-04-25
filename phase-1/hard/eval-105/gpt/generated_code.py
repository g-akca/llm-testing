# entry_point: by_length

def by_length(arr):
    """
    Given an array (list) of integers, keep only the digits 1–9 (inclusive),
    sort that sub-array in ascending order, reverse it, and then replace each
    digit with its corresponding English name.

    Mapping:
        1 → "One", 2 → "Two", …, 9 → "Nine"

    Examples
    --------
    >>> by_length([2, 1, 1, 4, 5, 8, 2, 3])
    ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']

    >>> by_length([])
    []

    >>> by_length([1, -1, 55])
    ['One']
    """
    # Mapping from digit to its word representation
    digit_to_word = {
        1: "One", 2: "Two", 3: "Three",
        4: "Four", 5: "Five", 6: "Six",
        7: "Seven", 8: "Eight", 9: "Nine",
    }

    # Keep only integers between 1 and 9 (inclusive)
    filtered_digits = [x for x in arr if isinstance(x, int) and 1 <= x <= 9]

    if not filtered_digits:        # nothing to convert
        return []

    # Sort ascending, then reverse to get descending order
    filtered_digits.sort()
    filtered_digits.reverse()

    # Convert each digit to its word
    return [digit_to_word[d] for d in filtered_digits]
