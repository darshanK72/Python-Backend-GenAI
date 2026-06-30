# 06 — Testing that code raises exceptions (unittest)
# Run: python 06_unittest_exceptions.py
#
# Good tests check error paths too, not just the happy path.
# assertRaises verifies that the expected exception is raised.

import unittest
from sample_code import divide, apply_discount, BankAccount

class TestExceptions(unittest.TestCase):
    # --- 1. assertRaises as a context manager (preferred) ---
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    # --- 2. Check the exception type for invalid input ---
    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            apply_discount(1000, 150)

    # --- 3. Also assert on the error message ---
    def test_error_message(self):
        with self.assertRaises(ValueError) as ctx:
            BankAccount(100).withdraw(500)
        self.assertEqual(str(ctx.exception), "insufficient balance")

    # --- 4. Match the message with a regex ---
    def test_message_regex(self):
        with self.assertRaisesRegex(ValueError, "positive"):
            BankAccount(100).deposit(-5)

if __name__ == "__main__":
    unittest.main(verbosity=2)
