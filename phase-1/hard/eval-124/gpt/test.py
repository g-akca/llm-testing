import unittest

# If the function resides in a separate file, e.g. `date_utils.py`,
# you would do: `from date_utils import valid_date`
# For this example we assume `valid_date` is available in the namespace.
from generated_code import valid_date   # adjust to the actual module name


class TestValidDate(unittest.TestCase):
    # ✅ 1. Valid edge-case: last day of a 31-day month
    def test_valid_31_day_month(self):
        self.assertTrue(valid_date("01-31-2024"))

    # ✅ 2. Invalid day overflow for a 30-day month
    def test_invalid_day_overflow(self):
        self.assertFalse(valid_date("04-31-2010"))

    # ✅ 3. Invalid month (out of range)
    def test_invalid_month(self):
        self.assertFalse(valid_date("13-15-1999"))

    # ✅ 4. Invalid delimiter/format
    def test_invalid_format_delimiter(self):
        self.assertFalse(valid_date("06/04/2020"))

    # ✅ 5. Empty string should be rejected
    def test_empty_string(self):
        self.assertFalse(valid_date(""))


if __name__ == "__main__":
    unittest.main()
