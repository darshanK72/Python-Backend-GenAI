# 02 — Patch where the name is used, not where it is defined
# Run: pytest 02_patch_side_effects.py -v

from unittest.mock import patch

from weather_client import fetch_temperature


@patch("weather_client.requests.get")
def test_http_error(mock_get):
    mock_get.side_effect = ConnectionError("network down")
    try:
        fetch_temperature("Pune", "key")
        assert False, "expected error"
    except ConnectionError:
        pass
