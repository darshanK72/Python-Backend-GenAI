# Shared pytest fixtures for lessons in this folder

import pytest


@pytest.fixture
def sample_user():
    return {"id": 1, "username": "learner", "role": "editor"}


@pytest.fixture
def api_base_url():
    return "http://testserver"
