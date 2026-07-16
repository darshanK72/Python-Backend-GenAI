"""Build and compile the corrective RAG LangGraph."""

from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from app.graph.nodes import make_generator_node, make_grader_node, make_retriever_node
from app.graph.state import RAGState
from app.services.llm_service import LLMService
from app.services.vector_store import VectorStore


# build_graph - compile the retrieve → grade → generate StateGraph
def build_graph(
    service: LLMService | None = None,
    store: VectorStore | None = None,
):
    """Compile the retrieve → grade → generate StateGraph."""
    llm = service or LLMService()
    vector_store = store or VectorStore.load_local()

    builder = StateGraph(RAGState)
    builder.add_node("retriever", make_retriever_node(vector_store))
    builder.add_node("grader", make_grader_node(llm))
    builder.add_node("generator", make_generator_node(llm))

    builder.add_edge(START, "retriever")
    builder.add_edge("retriever", "grader")
    builder.add_edge("grader", "generator")
    builder.add_edge("generator", END)
    return builder.compile()
