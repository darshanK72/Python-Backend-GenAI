"""FastMCP server exposing RAG, database, and session history tools."""

from __future__ import annotations

from fastmcp import FastMCP

from app.config import MCP_SERVER_HOST, MCP_SERVER_PORT
from app.services.db_tool import db_query as run_db_query
from app.services.rag_tool import rag_search as run_rag_search
from app.services.session_store import format_history

# mcp - FastMCP application hosting the three worker tools
mcp = FastMCP("unified-engineering-assistant")


# rag_search - FAISS top-k knowledge-base search tool
@mcp.tool
def rag_search(query: str) -> str:
    """Search the engineering knowledge base and return top matching chunks."""
    return run_rag_search(query)


# db_query - natural-language SQLite analytics tool
@mcp.tool
def db_query(question: str) -> str:
    """Run a natural-language query against project_management.db."""
    return run_db_query(question)


# get_session_history - session recap tool keyed by thread_id
@mcp.tool
def get_session_history(thread_id: str) -> str:
    """Return a formatted recap of prior queries for the session thread."""
    return format_history(thread_id)


# main - run the MCP server over HTTP for the assistant client
if __name__ == "__main__":
    mcp.run(transport="streamable-http", host=MCP_SERVER_HOST, port=MCP_SERVER_PORT)
