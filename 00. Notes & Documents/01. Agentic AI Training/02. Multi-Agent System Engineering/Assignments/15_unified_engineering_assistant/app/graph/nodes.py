"""Supervisor and specialist worker nodes."""

from __future__ import annotations

from app.cli.output import print_answer, print_route
from app.graph.state import AssistantState, SessionEntry
from app.schemas.prompts import (
    AMBIGUOUS_NOTE,
    RAG_SYNTHESIS_SYSTEM,
    RAG_SYNTHESIS_USER,
)
from app.services.llm_service import LLMService
from app.services.mcp_client import MCPClientWrapper
from app.services.router import classify_query, is_ambiguous
from app.services.session_store import append_entry


# _history_context - format prior session turns for supervisor / RAG prompts
def _history_context(history: list[SessionEntry]) -> str:
    if not history:
        return "None"
    return "\n".join(
        f"Turn {item['turn']}: [{item['worker']}] {item['query']}"
        for item in history
    )


# _record_session - append one turn to the shared session store and return it
def _record_session(state: AssistantState, summary: str) -> SessionEntry:
    entry = SessionEntry(
        turn=state["turn"],
        query=state["query"],
        worker=state["route"],
        summary=summary,
    )
    append_entry(state["thread_id"], entry)
    return entry


# make_supervisor_node - build the supervisor classification node
def make_supervisor_node(service: LLMService):
    # supervisor_node - classify the query and set the route field
    def supervisor_node(state: AssistantState) -> AssistantState:
        history = list(state.get("session_history", []))
        turn = len(history) + 1
        route = classify_query(
            state["query"],
            _history_context(history),
            service=service,
        )
        print_route(route, state["query"])
        return AssistantState(
            messages=[],
            query=state["query"],
            route=route,
            worker_result=state.get("worker_result", ""),
            session_history=[],
            thread_id=state["thread_id"],
            turn=turn,
            finished=route == "FINISH",
        )

    return supervisor_node


# make_rag_worker_node - build the FAISS / MCP rag_search worker
def make_rag_worker_node(service: LLMService, mcp: MCPClientWrapper):
    # rag_worker_node - search the knowledge base and synthesise an answer
    def rag_worker_node(state: AssistantState) -> AssistantState:
        chunks = mcp.call_tool("rag_search", {"query": state["query"]})
        session_context = _history_context(state.get("session_history", []))
        answer = service.chat(
            [
                {"role": "system", "content": RAG_SYNTHESIS_SYSTEM},
                {
                    "role": "user",
                    "content": RAG_SYNTHESIS_USER.format(
                        query=state["query"],
                        results=chunks,
                    )
                    + (
                        f"\n\nSession context:\n{session_context}"
                        if is_ambiguous(state["query"])
                        else ""
                    ),
                },
            ],
            temperature=0.2,
        ).strip()
        if is_ambiguous(state["query"]):
            answer = f"{AMBIGUOUS_NOTE}\n\n{answer}"
        entry = _record_session(state, answer[:200])
        print_answer(answer)
        return AssistantState(
            messages=[{"role": "assistant", "content": answer}],
            query=state["query"],
            route=state["route"],
            worker_result=answer,
            session_history=[entry],
            thread_id=state["thread_id"],
            turn=state["turn"],
            finished=False,
        )

    return rag_worker_node


# make_db_worker_node - build the SQLite / MCP db_query worker
def make_db_worker_node(mcp: MCPClientWrapper):
    # db_worker_node - answer project-data questions via MCP
    def db_worker_node(state: AssistantState) -> AssistantState:
        answer = mcp.call_tool("db_query", {"question": state["query"]})
        entry = _record_session(state, answer[:200])
        print_answer(answer)
        return AssistantState(
            messages=[{"role": "assistant", "content": answer}],
            query=state["query"],
            route=state["route"],
            worker_result=answer,
            session_history=[entry],
            thread_id=state["thread_id"],
            turn=state["turn"],
            finished=False,
        )

    return db_worker_node


# make_memory_worker_node - build the session-history MCP worker
def make_memory_worker_node(mcp: MCPClientWrapper):
    # memory_worker_node - return a recap of prior queries for this thread
    def memory_worker_node(state: AssistantState) -> AssistantState:
        answer = mcp.call_tool(
            "get_session_history",
            {"thread_id": state["thread_id"]},
        )
        entry = _record_session(state, answer[:200])
        print_answer(answer)
        return AssistantState(
            messages=[{"role": "assistant", "content": answer}],
            query=state["query"],
            route=state["route"],
            worker_result=answer,
            session_history=[entry],
            thread_id=state["thread_id"],
            turn=state["turn"],
            finished=False,
        )

    return memory_worker_node


# make_finish_node - build the session-complete terminal node
def make_finish_node():
    # finish_node - emit a goodbye message when the supervisor chooses FINISH
    def finish_node(state: AssistantState) -> AssistantState:
        message = "Session complete. Goodbye."
        print_answer(message)
        return AssistantState(
            messages=[{"role": "assistant", "content": message}],
            query=state["query"],
            route="FINISH",
            worker_result=message,
            session_history=[],
            thread_id=state["thread_id"],
            turn=state["turn"],
            finished=True,
        )

    return finish_node
