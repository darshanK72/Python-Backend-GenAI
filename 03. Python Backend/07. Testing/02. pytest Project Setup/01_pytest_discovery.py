# 01 — pytest discovery and naming
# Run: pytest 01_pytest_discovery.py -v
#
# Real projects use test_*.py for auto-discovery.
# These lessons use number prefixes — run files explicitly.


def add(a: int, b: int) -> int:
    return a + b


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -2) == -3


class TestAdd:
    def test_zero(self):
        assert add(0, 0) == 0
