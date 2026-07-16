"""Tests for supervisor routing."""

from app.services.router import classify_query, is_ambiguous


# test_routes_rag_query - test that concept questions route to rag
def test_routes_rag_query() -> None:
    assert (
        classify_query("What is the difference between microservices and a monolith?")
        == "rag"
    )


# test_routes_db_query - test that project-data questions route to db
def test_routes_db_query() -> None:
    assert classify_query("Which of our tasks are currently blocked?") == "db"


# test_routes_memory_query - test that session-recap questions route to memory
def test_routes_memory_query() -> None:
    assert classify_query("What have I asked you so far?") == "memory"


# test_ambiguous_query_routes_to_rag - test Query 4 hybrid ambiguity routes to rag
def test_ambiguous_query_routes_to_rag() -> None:
    query = (
        "Based on our conversation, are there DevOps best practices I should "
        "apply to the blocked tasks?"
    )
    assert is_ambiguous(query)
    assert classify_query(query) == "rag"
