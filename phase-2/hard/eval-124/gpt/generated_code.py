import re

def valid_date(date: str) -> bool:
    """
    You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months
       1,3,5,7,8,10,12. And the number of days is not less than 1 or higher
       than 30 days for months 4,6,9,11. And, the number of days is not less
       than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    Examples
    --------
    >>> valid_date('03-11-2000')
    True
    >>> valid_date('15-01-2012')
    False
    >>> valid_date('04-0-2040')
    False
    >>> valid_date('06-04-2020')
    True
    >>> valid_date('06/04/2020')
    False
    """
    if not date:
        return False

    # Ensure the string strictly matches mm-dd-yyyy with two-digit month/day
    match = re.fullmatch(r"(?P<mm>\d{2})-(?P<dd>\d{2})-(?P<yyyy>\d{4})", date)
    if not match:
        return False

    month = int(match.group("mm"))
    day   = int(match.group("dd"))

    # Rule 3: month range
    if month < 1 or month > 12:
        return False

    # Rule 2: day range per month
    if month in {1, 3, 5, 7, 8, 10, 12}:       # 31-day months
        return 1 <= day <= 31
    elif month in {4, 6, 9, 11}:               # 30-day months
        return 1 <= day <= 30
    else:                                      # February
        return 1 <= day <= 29
