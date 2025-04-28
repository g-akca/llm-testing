import unittest

# assuming valid_date is defined in the same module or imported appropriately
from generated_code import valid_date


class TestValidDate(unittest.TestCase):
    def test_valid_standard_date(self):
        """Typical valid date in a 31-day month."""
        self.assertTrue(valid_date("03-11-2000"))

    def test_invalid_month(self):
        """Month number out of range (15)."""
        self.assertFalse(valid_date("15-01-2012"))

    def test_invalid_day_for_month(self):
        """Day exceeds limit for April (only 30 days)."""
        self.assertFalse(valid_date("04-31-2023"))

    def test_wrong_separator(self):
        """Date uses '/' instead of '-'."""
        self.assertFalse(valid_date("06/04/2020"))

    def test_february_29_allowed(self):
        """February 29 is accepted regardless of leap year check (per spec)."""
        self.assertTrue(valid_date("02-29-2025"))


if __name__ == "__main__":
    unittest.main()
