import unittest

# Assuming the function check_dict_case is in a file named 'dict_checker.py'
from generated_code import check_dict_case 
# If the function is in the same file, you don't need the import above.

class TestCheckDictCase(unittest.TestCase):

    def test_empty_dict(self):
        """Test that an empty dictionary returns False."""
        self.assertFalse(check_dict_case({}))

    def test_all_lower_case(self):
        """Test a dictionary with all lowercase string keys."""
        self.assertTrue(check_dict_case({"a": "apple", "b": "banana"}))
        self.assertTrue(check_dict_case({"key1": 1, "key2": 2}))

    def test_all_upper_case(self):
        """Test a dictionary with all uppercase string keys."""
        self.assertTrue(check_dict_case({"STATE": "NC", "ZIP": "12345"}))
        self.assertTrue(check_dict_case({"FIRST": "A", "SECOND": "B"}))

    def test_mixed_case(self):
        """Test a dictionary with mixed case string keys."""
        self.assertFalse(
            check_dict_case({"a": "apple", "A": "banana", "B": "banana"})
        )
        self.assertFalse(
            check_dict_case({"Name": "John", "Age": "36", "City": "Houston"})
        )
        self.assertFalse(check_dict_case({"lower": 1, "UPPER": 2}))

    def test_non_string_keys(self):
        """Test a dictionary containing non-string keys."""
        self.assertFalse(
            check_dict_case({"a": "apple", 8: "banana", "b": "orange"})
        )
        self.assertFalse(check_dict_case({1: "one", 2: "two"}))
        self.assertFalse(check_dict_case({"KEY": "value", None: "none"}))


# To run the tests from the command line:
# python -m unittest your_file_name.py
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
