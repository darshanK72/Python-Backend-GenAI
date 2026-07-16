"""Tests for SQL validation."""

from app.services.sql_validator import detect_write_intent, validate_sql


# test_validator_rejects_forbidden_verb - test DELETE is rejected with a specific message
def test_validator_rejects_forbidden_verb(db_conn, schema_map) -> None:
    is_valid, error = validate_sql(
        "DELETE FROM tasks WHERE status = 'blocked'",
        db_conn,
        schema_map,
    )
    assert is_valid is False
    assert "forbidden verb DELETE" in error


# test_detect_write_intent_delete - test delete/remove questions map to DELETE
def test_detect_write_intent_delete() -> None:
    assert detect_write_intent("delete team member Alice Chen") == "DELETE"
    assert detect_write_intent("Please remove Alice Chen") == "DELETE"
    assert detect_write_intent("How many tasks are currently blocked?") is None


# test_validator_rejects_unknown_table - test unknown tables list available tables
def test_validator_rejects_unknown_table(db_conn, schema_map) -> None:
    is_valid, error = validate_sql(
        "SELECT name FROM employees",
        db_conn,
        schema_map,
    )
    assert is_valid is False
    assert "Table 'employees' does not exist" in error
    assert "projects" in error


# test_validator_rejects_unknown_column - test unknown columns list available columns
def test_validator_rejects_unknown_column(db_conn, schema_map) -> None:
    is_valid, error = validate_sql(
        "SELECT assigneed FROM tasks",
        db_conn,
        schema_map,
    )
    assert is_valid is False
    assert "Column 'assigneed' does not exist in table 'tasks'" in error
    assert "assignee" in error


# test_validator_accepts_valid_select - test a correct COUNT query passes validation
def test_validator_accepts_valid_select(db_conn, schema_map) -> None:
    is_valid, error = validate_sql(
        "SELECT COUNT(*) FROM tasks WHERE status = 'blocked'",
        db_conn,
        schema_map,
    )
    assert is_valid is True
    assert error == ""


# test_validator_accepts_select_column_alias - test AS aliases are not treated as table columns
def test_validator_accepts_select_column_alias(db_conn, schema_map) -> None:
    is_valid, error = validate_sql(
        "SELECT COUNT(*) AS blocked_task_count FROM tasks WHERE status = 'blocked'",
        db_conn,
        schema_map,
    )
    assert is_valid is True
    assert error == ""
