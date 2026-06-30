# 11 — Mocking with unittest.mock
# Run:  python 11_mocking_basics.py
#       pytest "11_mocking_basics.py" -v
#
# Mocking replaces a real dependency (network, time, random, database) with a
# fake object you control, so tests stay fast, repeatable, and offline.

import unittest
from unittest.mock import Mock, patch

# --- 1. Mock: a fake object that records how it was called ---
def notify(sender, message):
    sender.send(message)          # sender is some external service
    return True

class TestMock(unittest.TestCase):
    def test_notify_calls_send(self):
        fake_sender = Mock()                       # stand-in object
        notify(fake_sender, "hello")
        fake_sender.send.assert_called_once_with("hello")

    # --- 2. Configure a return value on the mock ---
    def test_mock_return_value(self):
        service = Mock()
        service.get_status.return_value = "OK"
        self.assertEqual(service.get_status(), "OK")

# --- 3. patch: temporarily replace something real during a test ---
# Function that depends on the current time:
import time
def is_business_hours():
    hour = time.localtime().tm_hour
    return 9 <= hour < 17

class TestPatch(unittest.TestCase):
    # Replace time.localtime so the test is deterministic.
    @patch("time.localtime")
    def test_open(self, mock_localtime):
        mock_localtime.return_value = time.struct_time((2026, 1, 1, 10, 0, 0, 0, 1, 0))
        self.assertTrue(is_business_hours())

    @patch("time.localtime")
    def test_closed(self, mock_localtime):
        mock_localtime.return_value = time.struct_time((2026, 1, 1, 22, 0, 0, 0, 1, 0))
        self.assertFalse(is_business_hours())

# --- 4. patch as a context manager (instead of decorator) ---
def get_random_winner(players):
    import random
    return random.choice(players)

class TestContextPatch(unittest.TestCase):
    def test_winner(self):
        with patch("random.choice", return_value="Darshan"):
            self.assertEqual(get_random_winner(["a", "b"]), "Darshan")

if __name__ == "__main__":
    unittest.main(verbosity=2)

# pytest equivalent uses the `monkeypatch` fixture or the pytest-mock plugin,
# but unittest.mock (shown here) works in both unittest and pytest.
