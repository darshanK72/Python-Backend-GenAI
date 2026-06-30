# sample_code — small module that the test lessons import and test
# This file holds the "code under test" so each lesson can focus on testing.

def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b


def is_even(n):
    return n % 2 == 0


def apply_discount(price, percent):
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return price * (100 - percent) / 100


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.balance:
            raise ValueError("insufficient balance")
        self.balance -= amount
        return self.balance
