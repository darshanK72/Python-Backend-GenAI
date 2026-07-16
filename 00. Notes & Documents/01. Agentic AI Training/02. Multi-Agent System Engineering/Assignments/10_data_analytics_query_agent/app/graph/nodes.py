"""Reflection-loop graph nodes for SQL generation and validation."""

from __future__ import annotations

import sqlite3

from app.cli.output import print_generated_sql, print_retry, print_validation
from app.config import FAILURE_MESSAGE
from app.graph.state import AnalyticsState
from app.schemas.prompts import (
    GENERATOR_FEEDBACK,
    GENERATOR_SYSTEM,
    GENERATOR_USER,
    SUMMARIZER_SYSTEM,
    SUMMARIZER_USER,
)
from app.services.database import execute_select
from app.services.llm_service import LLMService
from app.services.sql_parser import extract_sql
from app.services.sql_validator import (
    detect_write_intent,
    forbidden_sql_for_verb,
    is_forbidden_verb_error,
    validate_sql,
)


# make_generator_node - create the SQL generator node
def make_generator_node(service: LLMService):
    """Create the SQL generator node."""

    def generator_node(state: AnalyticsState) -> AnalyticsState:
        # Block mutation requests before the LLM can rewrite them as SELECT.
        write_verb = detect_write_intent(state["question"])
        if write_verb:
            sql = forbidden_sql_for_verb(write_verb)
            print_generated_sql(sql)
            return AnalyticsState(
                question=state["question"],
                schema_info=state["schema_info"],
                sql_query=sql,
                validation_error="",
                retry_count=state["retry_count"],
                is_valid=False,
                columns=state["columns"],
                rows=state["rows"],
                summary=state["summary"],
                answer=state["answer"],
            )

        feedback = ""
        if state["validation_error"]:
            feedback = GENERATOR_FEEDBACK.format(error=state["validation_error"])
            print_retry(state["retry_count"], state["validation_error"])

        sql = extract_sql(
            service.chat(
                [
                    {"role": "system", "content": GENERATOR_SYSTEM},
                    {
                        "role": "user",
                        "content": GENERATOR_USER.format(
                            schema=state["schema_info"],
                            question=state["question"],
                            feedback=feedback,
                        ),
                    },
                ],
                temperature=0.0,
            )
        )
        print_generated_sql(sql)
        return AnalyticsState(
            question=state["question"],
            schema_info=state["schema_info"],
            sql_query=sql,
            validation_error="",
            retry_count=state["retry_count"],
            is_valid=False,
            columns=state["columns"],
            rows=state["rows"],
            summary=state["summary"],
            answer=state["answer"],
        )

    return generator_node


# make_validator_node - create the SQL validator node
def make_validator_node(conn: sqlite3.Connection, schema: dict[str, list[str]]):
    """Create the SQL validator node."""

    def validator_node(state: AnalyticsState) -> AnalyticsState:
        is_valid, error = validate_sql(state["sql_query"], conn, schema)
        print_validation(is_valid, error)
        retry_count = state["retry_count"]
        if not is_valid:
            retry_count += 1
        return AnalyticsState(
            question=state["question"],
            schema_info=state["schema_info"],
            sql_query=state["sql_query"],
            validation_error=error,
            retry_count=retry_count,
            is_valid=is_valid,
            columns=state["columns"],
            rows=state["rows"],
            summary=state["summary"],
            answer=state["answer"],
        )

    return validator_node


# make_executor_node - create the SELECT execution node
def make_executor_node(conn: sqlite3.Connection):
    """Create the SELECT execution node."""

    def executor_node(state: AnalyticsState) -> AnalyticsState:
        columns, rows = execute_select(state["sql_query"], conn)
        return AnalyticsState(
            question=state["question"],
            schema_info=state["schema_info"],
            sql_query=state["sql_query"],
            validation_error="",
            retry_count=state["retry_count"],
            is_valid=True,
            columns=columns,
            rows=rows,
            summary=state["summary"],
            answer=state["answer"],
        )

    return executor_node


# make_summarizer_node - create the plain-English summarizer node
def make_summarizer_node(service: LLMService):
    """Create the plain-English summarizer node."""

    def summarizer_node(state: AnalyticsState) -> AnalyticsState:
        summary = service.chat(
            [
                {"role": "system", "content": SUMMARIZER_SYSTEM},
                {
                    "role": "user",
                    "content": SUMMARIZER_USER.format(
                        question=state["question"],
                        sql=state["sql_query"],
                        columns=state["columns"],
                        rows=state["rows"],
                    ),
                },
            ],
            temperature=0.2,
        ).strip()
        answer = format_answer(state["sql_query"], state["columns"], state["rows"], summary)
        return AnalyticsState(
            question=state["question"],
            schema_info=state["schema_info"],
            sql_query=state["sql_query"],
            validation_error="",
            retry_count=state["retry_count"],
            is_valid=True,
            columns=state["columns"],
            rows=state["rows"],
            summary=summary,
            answer=answer,
        )

    return summarizer_node


# make_failure_node - create the max-retry / safety-rejection failure node
def make_failure_node():
    """Create the max-retry / safety-rejection failure node."""

    def failure_node(state: AnalyticsState) -> AnalyticsState:
        error = state["validation_error"]
        answer = error if is_forbidden_verb_error(error) else FAILURE_MESSAGE
        return AnalyticsState(
            question=state["question"],
            schema_info=state["schema_info"],
            sql_query=state["sql_query"],
            validation_error=error,
            retry_count=state["retry_count"],
            is_valid=False,
            columns=[],
            rows=[],
            summary="",
            answer=answer,
        )

    return failure_node


# format_answer - build SQL + results + summary output for the user
def format_answer(sql: str, columns: list[str], rows: list[tuple], summary: str) -> str:
    """Build SQL + results + summary output for the user."""
    return (
        f"SQL:\n```sql\n{sql}\n```\n\n"
        f"Results:\nColumns: {columns}\nRows: {rows}\n\n"
        f"Summary: {summary}"
    )
