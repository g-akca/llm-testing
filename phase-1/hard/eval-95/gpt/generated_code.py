def check_dict_case(d):
    """
    Given a dictionary, return True if **all** keys are strings in **lower case**
    **or** **all** keys are strings in **upper case**; otherwise return False.
    The function returns False for an empty dictionary.

    Examples
    --------
    >>> check_dict_case({"a": "apple", "b": "banana"})
    True
    >>> check_dict_case({"a": "apple", "A": "banana", "B": "banana"})
    False
    >>> check_dict_case({"a": "apple", 8: "banana"})
    False
    >>> check_dict_case({"Name": "John", "Age": "36", "City": "Houston"})
    False
    >>> check_dict_case({"STATE": "NC", "ZIP": "12345"})
    True
    """
    # Dictionary must not be empty
    if not d:
        return False

    # All keys must be strings
    if not all(isinstance(k, str) for k in d):
        return False

    all_lower = all(k.islower() for k in d)
    all_upper = all(k.isupper() for k in d)

    return all_lower or all_upper
