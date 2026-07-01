# 02 — pytest fixture builds test data
# Run: pytest 02_fixture_factories.py -v

import pytest


@pytest.fixture
def user_factory():
    def _factory(**overrides):
        data = {"id": 1, "username": "learner", "role": "viewer"}
        data.update(overrides)
        return data

    return _factory


def test_admin_user(user_factory):
    user = user_factory(role="admin")
    assert user["role"] == "admin"


def test_default_user(user_factory):
    user = user_factory()
    assert user["username"] == "learner"
