import unittest
from typing import List

# --------- copy or import your implementation here -----------------
# For demonstration, we import it directly assuming it's in the same file.
# If it's in a separate module (e.g., my_module.py), change the import line:
# from my_module import generate_integers

def generate_integers(a: int, b: int) -> List[int]:
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Both a and b must be integers.")
    if a <= 0 or b <= 0:
        raise ValueError("Both a and b must be positive integers (> 0).")

    low, high = sorted((a, b))
    even_digits = (2, 4, 6, 8)
    return [d for d in even_digits if low <= d <= high]


# ----------------------------- tests --------------------------------
class TestGenerateIntegers(unittest.TestCase):
    def test_standard_range(self):
        """Ascending range that includes all even digits."""
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_descending_range(self):
        """Descending inputs should still produce ascending output."""
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_no_even_digits(self):
        """Range containing no even single-digit integers returns empty list."""
        self.assertEqual(generate_integers(10, 14), [])

    def test_single_value_edge(self):
        """Edge case where low == high and equals an even digit."""
        self.assertEqual(generate_integers(4, 4), [4])

    def test_invalid_input(self):
        """Non-positive input should raise ValueError."""
        with self.assertRaises(ValueError):
            generate_integers(0, 5)


# Optional: enable running with `python test_file.py`
if __name__ == "__main__":
    unittest.main()
