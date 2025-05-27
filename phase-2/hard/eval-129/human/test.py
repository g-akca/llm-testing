# @Authors
# Student Names: Barış Türker, Gökçe Akca, Necip Baha Sağıroğlu
# Student IDs: 150170113, 150210046, 150220727

import sys
import os
import importlib
import unittest

if len(sys.argv) != 2 or sys.argv[1] not in ["gpt", "gemini"]:
    print("Usage: python test.py [gpt|gemini]")
    sys.exit(1)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
prompt = sys.argv.pop(1)
module_name = f"{prompt}.generated_code"
module = importlib.import_module(module_name)
minPath = getattr(module, "minPath")

class TestMinPath(unittest.TestCase):
    def test_example(self):
        self.assertEqual(minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), [1, 2, 1])
        self.assertEqual(minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1), [1])
        self.assertEqual(minPath([[9, 8, 7], [6, 5, 4], [3, 2, 1]], 3), [1, 2, 1])
        self.assertEqual(minPath([[1, 2], [3, 4]], 4), [1, 2, 1, 2])

    def test_boundary(self):
        self.assertEqual(minPath([[1, 2], [3, 4]], 1), [1])
        self.assertEqual(minPath([[1, 2], [3, 4]], 3), [1, 2, 1])

    def test_3x3_grid(self):
        self.assertEqual(minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 5), [1, 4, 1, 4, 1])

    def test_4x4_grid(self):
        self.assertEqual(minPath([[16, 15, 14, 13], [5, 6, 7, 12], [4, 1, 8, 11], [3, 2, 9, 10]], 4), [1, 2, 1, 2])

    def test_large_k_small_grid(self):
        self.assertEqual(minPath([[1, 2], [3, 4]], 10), [1, 2, 1, 2, 1, 2, 1, 2, 1, 2])

if __name__ == "__main__":
    unittest.main()
