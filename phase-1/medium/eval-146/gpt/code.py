def specialFilter(nums):
    """
    Write a function that takes an array of numbers as input and returns
    the number of elements in the array that are greater than 10 and whose
    first and last digits are both odd (1, 3, 5, 7, 9).

    Examples
    --------
    >>> specialFilter([15, -73, 14, -15])
    1
    >>> specialFilter([33, -2, -3, 45, 21, 109])
    2
    """
    count = 0
    odd_digits = {"1", "3", "5", "7", "9"}

    for n in nums:
        if n > 10:  # must be greater than 10
            s = str(n)
            # first and last character representation must be an odd digit
            if s[0] in odd_digits and s[-1] in odd_digits:
                count += 1
    return count
