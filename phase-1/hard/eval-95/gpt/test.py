import unittest

from generated_code import check_dict_case  # replace `your_module` with the actual filename

class TestCheckDictCase(unittest.TestCase):

    def test_all_lower_keys(self):
        data = {"a": 1, "b": 2, "c": 3}
        self.assertTrue(check_dict_case(data))

    def test_all_upper_keys(self):
        data = {"FOO": "bar", "BAR": "baz"}
        self.assertTrue(check_dict_case(data))

    def test_mixed_case_keys(self):
        data = {"a": 1, "B": 2}
        self.assertFalse(check_dict_case(data))

    def test_non_string_key(self):
        data = {"a": 1, 2: "b"}
        self.assertFalse(check_dict_case(data))

    def test_empty_dict(self):
        self.assertFalse(check_dict_case({}))

if __name__ == "__main__":
    unittest.main()
