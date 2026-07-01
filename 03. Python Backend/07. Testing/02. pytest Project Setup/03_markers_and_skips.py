# 03 — pytest markers, skip, and xfail
# Run: pytest 03_markers_and_skips.py -v
#       pytest 03_markers_and_skips.py -v -m integration

import os
import sys

import pytest

pytestmark = []


def test_always_runs():
    assert True


@pytest.mark.integration
def test_integration_example():
    assert os.getenv("RUN_INTEGRATION", "0") == "1" or True


@pytest.mark.skipif(sys.platform != "linux", reason="demo skip on non-Linux")
def test_linux_only_demo():
    assert True


@pytest.mark.xfail(reason="demo expected failure")
def test_known_bug():
    assert 1 == 2
