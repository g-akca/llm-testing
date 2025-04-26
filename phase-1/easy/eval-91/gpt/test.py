import unittest

# Assume `is_bored` is available in the same module / imported accordingly.
from code import is_bored  # replace with actual import path if needed


class TestIsBored(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0, "Empty string should yield 0 boredoms")

    def test_no_i_sentence(self):
        text = "Hello world. How are you today?"
        self.assertEqual(is_bored(text), 0, "No sentence starts with 'I'")

    def test_single_i_sentence(self):
        text = "The sky is blue. The sun is shining. I love this weather"
        self.assertEqual(is_bored(text), 1, "Exactly one sentence starts with 'I'")

    def test_multiple_i_sentences_mixed_punctuation(self):
        text = "I am bored! Why is that? I do not know. Maybe tomorrow."
        self.assertEqual(is_bored(text), 2, "Two sentences start with 'I'")


if __name__ == "__main__":
    unittest.main()
