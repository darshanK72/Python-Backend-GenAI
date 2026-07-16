"""Tests for the MCP client."""

from __future__ import annotations

from unittest.mock import patch

import pytest

from app.services.mcp_client import MCPClientWrapper


# test_call_tool_uses_test_handler_without_network - test in-memory handler bypasses HTTP
def test_call_tool_uses_test_handler_without_network() -> None:
    client = MCPClientWrapper(tool_handler=lambda name, args: f"ok:{name}")

    result = client.call_tool("get_backlog", {})

    assert result == "ok:get_backlog"
    assert client.call_log[0]["tool"] == "get_backlog"


# test_call_tool_reports_server_down - test friendly error when MCP server is unreachable
def test_call_tool_reports_server_down() -> None:
    client = MCPClientWrapper(server_url="http://127.0.0.1:59999/mcp")

    with patch.object(client, "_open_client", side_effect=ConnectionRefusedError("refused")):
        with pytest.raises(RuntimeError, match="MCP server is not reachable"):
            client.call_tool("get_backlog", {})
