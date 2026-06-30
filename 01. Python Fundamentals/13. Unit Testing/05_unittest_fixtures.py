# 05 — unittest fixtures (setUp / tearDown)
# Run: python 05_unittest_fixtures.py
#
# Fixtures prepare a known starting state before each test and clean up after.
# This avoids repeating setup code in every test method.

import unittest
from sample_code import BankAccount

class TestBankAccount(unittest.TestCase):
    # --- Runs before EVERY test method ---
    def setUp(self):
        self.account = BankAccount(balance=100)

    # --- Runs after EVERY test method (cleanup) ---
    def tearDown(self):
        self.account = None

    def test_deposit(self):
        self.assertEqual(self.account.deposit(50), 150)

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(40), 60)

    def test_balance_is_isolated(self):
        # Each test gets a fresh account thanks to setUp.
        self.account.deposit(1000)
        self.assertEqual(self.account.balance, 1100)

class TestClassLevelFixture(unittest.TestCase):
    # --- Runs ONCE before all tests in this class (expensive setup) ---
    @classmethod
    def setUpClass(cls):
        cls.shared_data = list(range(1000))
        print("\n[setUpClass] built shared data once")

    @classmethod
    def tearDownClass(cls):
        print("[tearDownClass] cleaned up shared data")

    def test_length(self):
        self.assertEqual(len(self.shared_data), 1000)

    def test_first_value(self):
        self.assertEqual(self.shared_data[0], 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
