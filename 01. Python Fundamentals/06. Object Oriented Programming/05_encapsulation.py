# 05 — Encapsulation (hiding internal details)
# Run: python 05_encapsulation.py
#
# Encapsulation = keep data safe and expose a clear interface.
# Python convention: prefix with _ for "internal use" (not enforced).

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance   # protected by convention

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > self._balance:
            print("Insufficient funds")
            return
        self._balance -= amount

    def get_balance(self):
        return self._balance

acct = BankAccount("Darshan", 1000)
acct.deposit(500)
acct.withdraw(200)
print("balance =", acct.get_balance())

# Can still access _balance directly (Python trusts you):
# print(acct._balance)

# --- Name mangling with __ (double underscore) ---
class Secret:
    def __init__(self):
        self.__pin = 1234   # becomes _Secret__pin

s = Secret()
# print(s.__pin)   # Uncomment -> AttributeError
print("mangled name exists:", hasattr(s, "_Secret__pin"))
