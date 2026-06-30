# 10 — pytest: exceptions, approx, and marks
# Install: pip install pytest
# Run:     pytest "10_pytest_exceptions_and_marks.py" -v
#
# Covers checking exceptions, comparing floats, and skipping / expected-fail.

import pytest
from sample_code import divide, apply_discount, BankAccount

# --- 1. pytest.raises: assert an exception is raised ---
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

# --- 2. Inspect the exception message ---
def test_invalid_discount_message():
    with pytest.raises(ValueError) as exc_info:
        apply_discount(1000, 150)
    assert "between 0 and 100" in str(exc_info.value)

# --- 3. Match the message with a regex shortcut ---
def test_withdraw_too_much():
    with pytest.raises(ValueError, match="insufficient"):
        BankAccount(100).withdraw(999)

# --- 4. Comparing floats safely with approx ---
def test_float_math():
    assert 0.1 + 0.2 == pytest.approx(0.3)

# --- 5. Skip a test (e.g. not ready / wrong platform) ---
@pytest.mark.skip(reason="example of skipping")
def test_not_ready():
    assert False

# --- 6. Skip conditionally ---
import sys
@pytest.mark.skipif(sys.version_info < (3, 10), reason="needs Python 3.10+")
def test_new_feature():
    assert True

# --- 7. Mark a test as expected to fail (known bug) ---
@pytest.mark.xfail(reason="demonstrates a known failing case")
def test_known_bug():
    assert divide(1, 0) == 0   # will fail -> reported as xfail, not error
