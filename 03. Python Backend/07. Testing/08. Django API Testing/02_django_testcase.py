# 02 — Django SimpleTestCase vs database tests
# Run: pytest 02_django_testcase.py -v

import pytest
from django.test import SimpleTestCase

from django_app import configure

configure()


class HealthTests(SimpleTestCase):
    def test_health_endpoint(self):
        r = self.client.get("/health/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()["status"], "ok")


def test_pytest_style_django_client():
    from django.test import Client

    r = Client().get("/health/")
    assert r.status_code == 200
