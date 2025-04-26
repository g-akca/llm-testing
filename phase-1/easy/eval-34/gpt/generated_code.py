from typing import List, Any


def unique(l: List[Any]) -> List[Any]:
    """
    Return sorted unique elements in a list.

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert to a set to drop duplicates, then sort the result.
    return sorted(set(l))


if __name__ == "__main__":
    # Simple manual test
    sample = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print(unique(sample))  # → [0, 2, 3, 5, 9, 123]
