from typing import List, Union

Number = Union[int, float]


def get_positive(l: List[Number]) -> List[Number]:
    """
    Return only positive numbers in the list.

    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [x for x in l if x > 0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
