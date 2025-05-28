from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate the Mean Absolute Deviation (MAD)
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the data:

        MAD = (1/n) * Σ |xᵢ − x̄|

    Args:
        numbers: A list of float (or int) values.

    Returns:
        The mean absolute deviation as a float.

    Raises:
        ValueError: If the input list is empty.

    Examples
    --------
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    >>> mean_absolute_deviation([5])
    0.0
    """
    if not numbers:
        raise ValueError("Input list 'numbers' must contain at least one value.")

    # Compute the arithmetic mean of the numbers
    n = len(numbers)
    mean_value = sum(numbers) / n

    # Compute the average absolute deviation from the mean
    mad = sum(abs(x - mean_value) for x in numbers) / n
    return mad
