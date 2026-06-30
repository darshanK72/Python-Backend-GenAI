# 09 — pytest parametrize (run one test with many inputs)
# Install: pip install pytest
# Run:     pytest "09_pytest_parametrize.py" -v
#
# Instead of copy-pasting a test for each input, parametrize feeds many
# (input -> expected) pairs into a single test. Each row is its own test.

import pytest
from sample_code import add, is_even, apply_discount

# --- 1. One parameter set: each tuple becomes a separate test case ---
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# --- 2. Single argument list ---
@pytest.mark.parametrize("number", [2, 4, 6, 100, 0])
def test_is_even_true(number):
    assert is_even(number)

@pytest.mark.parametrize("number", [1, 3, 5, 99])
def test_is_even_false(number):
    assert not is_even(number)

# --- 3. Named cases with pytest.param for readable test IDs ---
@pytest.mark.parametrize("price, percent, expected", [
    pytest.param(1000, 0, 1000, id="no-discount"),
    pytest.param(1000, 50, 500, id="half-off"),
    pytest.param(1000, 100, 0, id="free"),
])
def test_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected

# Run `pytest -v` and notice each row reports as its own PASS/FAIL line.
