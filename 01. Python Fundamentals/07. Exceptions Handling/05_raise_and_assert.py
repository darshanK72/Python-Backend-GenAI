# 05 — raise and assert
# Run: python 05_raise_and_assert.py

# --- 1. raise — throw an exception on purpose ---
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount > balance:
        raise ValueError("insufficient balance")
    return balance - amount

print("withdraw:", withdraw(1000, 200))

# withdraw(1000, 2000)   # Uncomment -> ValueError

# --- 2. Re-raise after logging ---
def process_age(age):
    try:
        if age < 0:
            raise ValueError("age cannot be negative")
        return age * 2
    except ValueError:
        print("logging error...")
        raise

# --- 3. assert — debug check (can be disabled with python -O) ---
def apply_discount(price, percent):
    assert 0 <= percent <= 100, "percent must be 0-100"
    return price * (100 - percent) / 100

print("price:", apply_discount(1000, 10))

# assert False, "this stops the program in debug mode"
