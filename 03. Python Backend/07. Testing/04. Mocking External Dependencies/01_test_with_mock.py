# 01 — Mock external HTTP with unittest.mock
# Run: pytest 01_test_with_mock.py -v

from unittest.mock import Mock, patch

from weather_client import fetch_temperature


@patch("weather_client.requests.get")
def test_fetch_temperature(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"temp_c": 22.5}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    temp = fetch_temperature("Pune", "fake-key")
    assert temp == 22.5
    mock_get.assert_called_once()
