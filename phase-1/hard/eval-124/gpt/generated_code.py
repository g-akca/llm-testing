def valid_date(date: str) -> bool:
    """
    Validate a date string of the form ``mm-dd-yyyy``.
    
    A date is considered **valid** if **all** of the following are true:
      1. `date` is a non-empty string.
      2. It is exactly in the form two-digit month, two-digit day, four-digit year,
         separated by *hyphens* (e.g. ``03-11-2000``).  
         Any other delimiter (such as “/”) or digit count is invalid.
      3. The month is between 1 and 12, inclusive.
      4. The day respects the maximum for that month:
         * 31 days for months 1, 3, 5, 7, 8, 10, 12  
         * 30 days for months 4, 6, 9, 11  
         * 29 days for month 2 (February) – leap-years are **ignored** by design.
    
    Examples
    --------
    >>> valid_date('03-11-2000')
    True
    >>> valid_date('15-01-2012')
    False
    >>> valid_date('06/04/2020')
    False
    """
    if not date:  # Rule 1
        return False

    parts = date.split('-')
    if len(parts) != 3:
        return False

    mm, dd, yyyy = parts

    # Ensure the exact digit counts required by the format (Rule 2)
    if not (len(mm) == 2 and len(dd) == 2 and len(yyyy) == 4):
        return False
    if not (mm.isdigit() and dd.isdigit() and yyyy.isdigit()):
        return False

    month, day = int(mm), int(dd)

    # Rule 3: valid month range
    if not (1 <= month <= 12):
        return False

    # Rule 4: day range depends on month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 1 <= day <= 31
    elif month in {4, 6, 9, 11}:
        return 1 <= day <= 30
    else:  # February
        return 1 <= day <= 29
