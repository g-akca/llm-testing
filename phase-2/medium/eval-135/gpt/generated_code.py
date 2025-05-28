def can_arrange(arr):
    """
    Returns the largest index i (0-based) such that
    arr[i] is **strictly less** than the element immediately
    preceding it (arr[i − 1]).  
    If no such index exists (i.e., the array is strictly
    increasing), returns -1.

    The array is guaranteed to contain no duplicate values.

    Examples
    --------
    >>> can_arrange([1, 2, 4, 3, 5])
    3
    >>> can_arrange([1, 2, 3])
    -1
    """
    # Traverse from the end so the first violation found is the largest index
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            return i
    return -1
