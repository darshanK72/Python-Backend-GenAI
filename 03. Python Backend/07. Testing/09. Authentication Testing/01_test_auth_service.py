# 01 — Test authentication logic
# Run: pytest 01_test_auth_service.py -v

import pytest

from auth_service import is_authorized, protected_action


def test_valid_key():
    assert is_authorized("demo-key")


def test_invalid_key():
    assert not is_authorized("wrong")


def test_protected_action_success():
    result = protected_action("demo-key")
    assert result["message"] == "secret data"


def test_protected_action_denied():
    with pytest.raises(PermissionError):
        protected_action("bad-key")
