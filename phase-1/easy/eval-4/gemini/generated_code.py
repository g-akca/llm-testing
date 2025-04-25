from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        # Return 0 for an empty list, as there's no deviation.
        # Alternatively, could raise ValueError depending on requirements.
        return 0.0

    mean = sum(numbers) / len(numbers)
    absolute_deviations = [abs(x - mean) for x in numbers]
    mad = sum(absolute_deviations) / len(numbers)
    return mad
