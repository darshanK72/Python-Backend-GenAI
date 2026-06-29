# 08 — pytest fixtures
# Install: pip install pytest
# Run:     pytest "08_pytest_fixtures.py" -v
#
# A fixture is a function decorated with @pytest.fixture that provides data
# or objects to tests. A test "requests" a fixture by naming it as a parameter.

import pytest
from sample_code import BankAccount

# --- 1. Basic fixture: returns a fresh object for each test ---
@pytest.fixture
def account():
    return BankAccount(balance=100)

def test_deposit(account):          # pytest injects the fixture by name
    assert account.deposit(50) == 150

def test_withdraw(account):         # gets its OWN fresh account
    assert account.withdraw(40) == 60

# --- 2. Fixture with setup AND teardown using yield ---
@pytest.fixture
def temp_account():
    print("\n[setup] creating account")
    acc = BankAccount(balance=500)
    yield acc                       # value handed to the test
    print("[teardown] discarding account")   # runs after the test

def test_temp(temp_account):
    temp_account.withdraw(100)
    assert temp_account.balance == 400

# --- 3. Fixture scope: reuse one instance across tests ---
# scope="module" -> created once per file instead of per test.
@pytest.fixture(scope="module")
def big_list():
    print("\n[setup] building big list once")
    return list(range(1000))

def test_len(big_list):
    assert len(big_list) == 1000

def test_first(big_list):
    assert big_list[0] == 0

# Tip: shared fixtures usually live in a conftest.py so many test files
# can use them without importing.
