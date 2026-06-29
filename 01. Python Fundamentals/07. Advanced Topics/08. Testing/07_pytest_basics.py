# 07 — pytest basics
# Install: pip install pytest
# Run:     pytest "07_pytest_basics.py" -v
#          pytest -v          (discovers all test_*.py / *_test.py files)
#
# pytest is the most popular third-party test framework. The big win:
# you write plain `assert` — no special assert methods, no classes required.

from sample_code import add, is_even, apply_discount

# --- 1. A test is just a function named test_* using plain assert ---
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_is_even():
    assert is_even(4)
    assert not is_even(7)

# --- 2. pytest shows rich failure output automatically ---
def test_discount():
    assert apply_discount(1000, 25) == 750

# --- 3. You can still group tests in a class (no inheritance needed) ---
class TestDiscount:
    def test_zero_percent(self):
        assert apply_discount(500, 0) == 500

    def test_full_percent(self):
        assert apply_discount(500, 100) == 0

# Notes:
#  - pytest auto-discovers files named test_*.py or *_test.py.
#  - This file is named 07_pytest_basics.py for ordering, so run it explicitly
#    with: pytest "07_pytest_basics.py"
#  - Add -v for verbose, -q for quiet, -k "add" to run tests matching a name.
