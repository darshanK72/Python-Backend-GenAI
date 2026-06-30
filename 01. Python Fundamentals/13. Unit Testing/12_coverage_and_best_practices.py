# 12 — Coverage and testing best practices
# Install: pip install pytest pytest-cov coverage
# Run tests with coverage:
#   pytest --cov=sample_code "12_coverage_and_best_practices.py"
#   coverage run -m pytest   &&   coverage report -m   (alternative)
#
# Coverage = how much of your code the tests actually execute. High coverage
# does NOT guarantee correctness, but low coverage means untested code.

from sample_code import BankAccount, apply_discount

# --- 1. The AAA pattern: Arrange, Act, Assert ---
def test_deposit_aaa():
    account = BankAccount(balance=100)   # Arrange: set up inputs
    new_balance = account.deposit(50)    # Act: call the thing under test
    assert new_balance == 150            # Assert: verify the result

# --- 2. Test the happy path AND the edge / error cases ---
def test_discount_happy_path():
    assert apply_discount(1000, 10) == 900

def test_discount_boundaries():
    assert apply_discount(1000, 0) == 1000
    assert apply_discount(1000, 100) == 0

# --- 3. One logical behaviour per test, with a descriptive name ---
def test_withdraw_reduces_balance():
    account = BankAccount(balance=200)
    account.withdraw(50)
    assert account.balance == 150

if __name__ == "__main__":
    # These plain asserts let the file also run with `python`.
    test_deposit_aaa()
    test_discount_happy_path()
    test_discount_boundaries()
    test_withdraw_reduces_balance()
    print("All best-practice example tests passed")

# Best practices checklist:
#  - Name tests test_<thing>_<expected_behaviour> so failures read like docs.
#  - Keep tests independent: no test should depend on another's side effects.
#  - Test behaviour (outputs), not internal implementation details.
#  - Cover edge cases: empty, zero, negative, boundaries, and errors.
#  - Keep tests fast; mock slow/external things (network, time, random).
#  - Aim for meaningful coverage, not 100% for its own sake.
