"""Tests for the CLI runner."""

from __future__ import annotations

import json
from unittest.mock import MagicMock

import pytest

from app.cli.runner import run_toolkit
from app.config import Settings
from app.services.llm_service import LLMService
from tests.conftest import VALID_JSON, make_chat_response


@pytest.fixture
def reports_file(tmp_path):
    reports = [f"report {index}" for index in range(1, 6)]
    path = tmp_path / "reports.json"
    path.write_text(json.dumps(reports), encoding="utf-8")
    return path


def test_run_toolkit_missing_reports_returns_error(tmp_path, capsys) -> None:
    exit_code = run_toolkit(tmp_path / "missing.json")

    assert exit_code == 1
    assert "not found" in capsys.readouterr().err.lower()


def test_run_toolkit_runs_all_strategies(reports_file, capsys) -> None:
    client = MagicMock()
    client.chat.completions.create.return_value = make_chat_response(VALID_JSON)
    settings = Settings.model_construct(openai_api_key="test-key")
    service = LLMService(settings=settings, client=client)

    exit_code = run_toolkit(reports_file, service=service)
    output = capsys.readouterr().out

    assert exit_code == 0
    assert output.count("[naive]") == 5
    assert output.count("[structured]") == 5
    assert output.count("[few-shot]") == 5
    assert "Structured valid outputs: 5/5" in output
    assert "Total tokens used:" in output
