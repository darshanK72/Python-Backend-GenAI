# 06 — Custom exception classes
# Run: python 06_custom_exceptions.py
#
# Inherit from Exception (or a built-in subclass).

class InsufficientFundsError(Exception):
    """Raised when a bank account has too little money."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Need {amount}, have {balance}")


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount


acct = BankAccount(500)
try:
    acct.withdraw(700)
except InsufficientFundsError as e:
    print("Caught:", e)
    print("balance was:", e.balance)

print("final balance:", acct.balance)
