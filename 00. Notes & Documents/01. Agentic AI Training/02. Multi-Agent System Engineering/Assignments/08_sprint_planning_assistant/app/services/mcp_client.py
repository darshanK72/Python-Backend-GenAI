"""MCP client — calls tools on a running MCP server (start mcp_server.py first)."""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from typing import Any

from app.cli.output import print_mcp_call
from app.config import MCP_SERVER_URL, get_settings

# _SERVER_DOWN_MESSAGE - user-facing error when the MCP server is not reachable
_SERVER_DOWN_MESSAGE = (
    "MCP server is not reachable at {url}.\n"
    "Start it in a separate terminal first:\n"
    "  python mcp_server.py"
)


class MCPClientWrapper:
    """Calls MCP tools on a server the developer has already started."""

    # __init__ - initialise with server URL or an in-memory test handler
    def __init__(
        self,
        server_url: str | None = None,
        *,
        tool_handler: Callable[[str, dict[str, Any]], str] | None = None,
    ) -> None:
        self.server_url = server_url or get_settings().mcp_server_url
        self._tool_handler = tool_handler
        self._client: Any = None
        self._loop: asyncio.AbstractEventLoop | None = None
        self.call_log: list[dict[str, Any]] = []

    # call_tool - invoke an MCP tool and log the call
    def call_tool(self, name: str, arguments: dict[str, Any] | None = None) -> str:
        """Invoke an MCP tool and return the result text."""
        args = arguments or {}
        if self._tool_handler is not None:
            result = self._tool_handler(name, args)
        else:
            try:
                result = self._call_remote_tool(name, args)
            except RuntimeError:
                raise
            except Exception as exc:
                raise RuntimeError(
                    _SERVER_DOWN_MESSAGE.format(url=self.server_url)
                ) from exc

        self.call_log.append({"tool": name, "arguments": args, "result": result})
        print_mcp_call(name, args, result)
        return result

    # _call_remote_tool - send one tool call to the running MCP server
    def _call_remote_tool(self, name: str, arguments: dict[str, Any]) -> str:
        self._ensure_client()
        if self._loop is None or self._client is None:
            raise RuntimeError(_SERVER_DOWN_MESSAGE.format(url=self.server_url))
        return self._loop.run_until_complete(self._async_call_tool(name, arguments))

    # _ensure_client - open the HTTP connection on the first live tool call
    def _ensure_client(self) -> None:
        if self._client is not None:
            return

        self._loop = asyncio.new_event_loop()
        try:
            self._loop.run_until_complete(self._open_client())
        except Exception as exc:
            self._loop.close()
            self._loop = None
            self._client = None
            raise RuntimeError(
                _SERVER_DOWN_MESSAGE.format(url=self.server_url)
            ) from exc

    # _open_client - connect to the running FastMCP HTTP server
    async def _open_client(self) -> None:
        from fastmcp import Client
        from fastmcp.client.transports import StreamableHttpTransport

        transport = StreamableHttpTransport(self.server_url)
        self._client = Client(transport)
        await self._client.__aenter__()

    # _async_call_tool - call a tool on the live MCP client
    async def _async_call_tool(self, name: str, arguments: dict[str, Any]) -> str:
        result = await self._client.call_tool(name, arguments)
        if hasattr(result, "data"):
            return str(result.data)
        return str(result)
