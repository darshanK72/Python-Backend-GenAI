# 02 — Shared fixtures via conftest.py
# Run: pytest 02_shared_fixtures.py -v


def test_user_has_role(sample_user):
    assert sample_user["role"] == "editor"


def test_base_url(api_base_url):
    assert api_base_url.startswith("http")
