import unittest
# Assuming the code generated previously is saved in a file named 'date_validator.py'
from generated_code import valid_date

class TestValidDate(unittest.TestCase):

    def test_valid_standard_date(self):
        """Test a standard valid date."""
        self.assertTrue(valid_date("03-11-2000"))
        self.assertTrue(valid_date("12-31-2023"))
        self.assertTrue(valid_date("01-01-1999"))

    def test_valid_february_date(self):
        """Test valid dates in February (including 29th)."""
        self.assertTrue(valid_date("02-29-2024")) # Leap year allowed up to 29
        self.assertTrue(valid_date("02-28-2021"))

    def test_invalid_format(self):
        """Test dates with incorrect formats."""
        self.assertFalse(valid_date("06/04/2020")) # Wrong separator
        self.assertFalse(valid_date("3-11-2000"))  # Month not 2 digits
        self.assertFalse(valid_date("03-1-2000"))  # Day not 2 digits
        self.assertFalse(valid_date("03-11-00"))   # Year not 4 digits
        self.assertFalse(valid_date("03-11-20000"))# Year too long

    def test_invalid_month_or_day_range(self):
        """Test dates with out-of-range month or day."""
        self.assertFalse(valid_date("13-01-2012")) # Invalid month > 12
        self.assertFalse(valid_date("00-01-2012")) # Invalid month == 0
        self.assertFalse(valid_date("04-31-2020")) # Invalid day > 30 for April
        self.assertFalse(valid_date("02-30-2021")) # Invalid day > 29 for Feb
        self.assertFalse(valid_date("01-00-2020")) # Invalid day == 0
        self.assertFalse(valid_date("08-32-2005")) # Invalid day > 31 for Aug

    def test_empty_or_none_input(self):
        """Test with empty string or None."""
        self.assertFalse(valid_date(""))
        # self.assertFalse(valid_date(None)) # The function expects a string

# To run the tests from the command line:
# python -m unittest your_test_file_name.py
# Or run this script directly if __name__ == "__main__": block is added:

if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
