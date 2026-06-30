# 03 — unittest basics (standard library, no install needed)
# Run: python 03_unittest_basics.py
#      python -m unittest 03_unittest_basics.py   (alternative)
#
# unittest is Python's built-in testing framework. Tests live in classes
# that inherit from unittest.TestCase, and each test is a method named test_*.

import unittest
from sample_code import add, is_even

class TestAdd(unittest.TestCase):
    # Each method starting with "test" is run automatically.
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        self.assertFalse(is_even(7))

# --- Run the tests when the file is executed directly ---
if __name__ == "__main__":
    unittest.main(verbosity=2)

# Output legend:
#   .   passed      F   failed (assertion)      E   error (exception)
