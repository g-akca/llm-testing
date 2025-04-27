import re

def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example:
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
    # 1. Check if the date string is empty
    if not date:
        return False

    # 4. Check the format using regex (mm-dd-yyyy)
    # This also implicitly checks length and separator characters
    if not re.match(r"^\d{2}-\d{2}-\d{4}$", date):
        return False

    try:
        # Split the date string into components
        parts = date.split("-")
        month_str, day_str, year_str = parts[0], parts[1], parts[2]

        # Convert parts to integers
        month = int(month_str)
        day = int(day_str)
        year = int(year_str) # year is parsed but not used in validation rules

        # 3. Validate month range
        if not (1 <= month <= 12):
            return False

        # 2. Validate day range based on month
        months_31_days = {1, 3, 5, 7, 8, 10, 12}
        months_30_days = {4, 6, 9, 11}

        if month in months_31_days:
            if not (1 <= day <= 31):
                return False
        elif month in months_30_days:
            if not (1 <= day <= 30):
                return False
        elif month == 2: # February
            if not (1 <= day <= 29):
                return False
        # This else should theoretically not be reached if month validation passed
        # else:
        #     return False # Should not happen if month is 1-12

    except ValueError:
        # This catches cases where parts are not valid integers
        # (e.g., 'ab-cd-efgh'), although regex already filters most of this.
        return False

    # If all checks passed
    return True

