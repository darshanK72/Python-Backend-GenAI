"""Validate generated SQL before execution."""

from __future__ import annotations

import re
import sqlite3

# FORBIDDEN_VERBS - DDL/DML verbs that must never appear in generated SQL
FORBIDDEN_VERBS = (
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "CREATE",
    "REPLACE",
    "TRUNCATE",
)

# WRITE_INTENT_PATTERNS - NL mutation verbs mapped to forbidden SQL verbs
WRITE_INTENT_PATTERNS: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"\b(delete|remove)\b", re.IGNORECASE), "DELETE"),
    (re.compile(r"\bdrop\b", re.IGNORECASE), "DROP"),
    (re.compile(r"\bupdate\b", re.IGNORECASE), "UPDATE"),
    (re.compile(r"\binsert\b", re.IGNORECASE), "INSERT"),
    (re.compile(r"\balter\b", re.IGNORECASE), "ALTER"),
    (re.compile(r"\bcreate\b", re.IGNORECASE), "CREATE"),
    (re.compile(r"\breplace\b", re.IGNORECASE), "REPLACE"),
    (re.compile(r"\btruncate\b", re.IGNORECASE), "TRUNCATE"),
)

# SQL_KEYWORDS - tokens that are not table or column identifiers
SQL_KEYWORDS = {
    "select", "from", "where", "join", "on", "and", "or", "group", "by", "order",
    "asc", "desc", "as", "inner", "left", "right", "outer", "count", "avg", "sum",
    "min", "max", "distinct", "in", "is", "not", "null", "like", "between", "having",
    "limit", "case", "when", "then", "else", "end", "with", "union", "all", "exists",
    "true", "false", "coalesce", "ifnull", "cast", "round", "strftime", "date",
}


# detect_write_intent - map mutation requests in natural language to a forbidden verb
def detect_write_intent(question: str) -> str | None:
    """Return the forbidden SQL verb if the question asks to mutate data."""
    for pattern, verb in WRITE_INTENT_PATTERNS:
        if pattern.search(question):
            return verb
    return None


# forbidden_sql_for_verb - build a representative DML/DDL statement for validation
def forbidden_sql_for_verb(verb: str) -> str:
    """Build a representative forbidden statement so the validator can reject it."""
    return f"{verb} FROM team_members"


# is_forbidden_verb_error - true when validation failed due to DDL/DML safety rules
def is_forbidden_verb_error(error: str) -> bool:
    """Return True when the validator rejected DDL/DML rather than a fixable schema error."""
    lower = error.lower()
    return "forbidden verb" in lower or "only select statements are permitted" in lower


# validate_sql - run forbidden-verb, schema, and EXPLAIN checks on a query
def validate_sql(
    sql: str,
    conn: sqlite3.Connection,
    schema: dict[str, list[str]],
) -> tuple[bool, str]:
    """Run forbidden-verb, schema, and EXPLAIN checks on a query."""
    cleaned = sql.strip().rstrip(";")
    if not cleaned:
        return False, "SQL syntax error: empty query"

    for verb in FORBIDDEN_VERBS:
        if re.search(rf"\b{verb}\b", cleaned, flags=re.IGNORECASE):
            return False, (
                f"SQL contains forbidden verb {verb}. "
                "Only SELECT statements are permitted"
            )

    if not cleaned.upper().startswith("SELECT"):
        return False, "Only SELECT statements are permitted"

    tables, alias_map = _extract_tables(cleaned)
    schema_lower = {name.lower(): name for name in schema}
    available_tables = ", ".join(sorted(schema))

    for table in tables:
        if table.lower() not in schema_lower:
            return False, (
                f"Table '{table}' does not exist. "
                f"Available tables: {available_tables}"
            )

    column_error = _validate_columns(cleaned, schema, tables, alias_map, schema_lower)
    if column_error:
        return False, column_error

    try:
        conn.execute(f"EXPLAIN {cleaned}")
    except sqlite3.Error as exc:
        return False, f"SQL syntax error: {exc}"

    return True, ""


# _extract_tables - extract table names and aliases from FROM/JOIN clauses
def _extract_tables(sql: str) -> tuple[list[str], dict[str, str]]:
    pattern = re.compile(
        r"\b(?:FROM|JOIN)\s+([a-zA-Z_][a-zA-Z0-9_]*)(?:\s+(?:AS\s+)?([a-zA-Z_][a-zA-Z0-9_]*))?",
        flags=re.IGNORECASE,
    )
    tables: list[str] = []
    alias_map: dict[str, str] = {}
    for match in pattern.finditer(sql):
        table = match.group(1)
        alias = match.group(2) or table
        tables.append(table)
        alias_map[alias.lower()] = table
        alias_map[table.lower()] = table
    return tables, alias_map


# _extract_column_aliases - collect SELECT output aliases introduced with AS
def _extract_column_aliases(sql: str) -> set[str]:
    """Collect SELECT output aliases introduced with AS (not real table columns)."""
    return {
        match.group(1).lower()
        for match in re.finditer(
            r"\bAS\s+([a-zA-Z_][a-zA-Z0-9_]*)\b",
            sql,
            flags=re.IGNORECASE,
        )
    }


# _validate_columns - verify referenced columns exist on the queried tables
def _validate_columns(
    sql: str,
    schema: dict[str, list[str]],
    tables: list[str],
    alias_map: dict[str, str],
    schema_lower: dict[str, str],
) -> str | None:
    stripped = re.sub(r"'[^']*'", "", sql)
    resolved_tables = [
        schema_lower.get(table.lower(), table) for table in tables
    ]
    column_aliases = _extract_column_aliases(stripped)

    for match in re.finditer(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\.([a-zA-Z_][a-zA-Z0-9_]*)\b", stripped):
        alias = match.group(1)
        column = match.group(2)
        table = alias_map.get(alias.lower(), alias)
        canonical = schema_lower.get(table.lower())
        if canonical is None:
            continue
        if not _column_exists(column, schema[canonical]):
            return _column_error(column, canonical, schema[canonical])

    tokens = re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b", stripped)
    for token in tokens:
        lower = token.lower()
        if lower in SQL_KEYWORDS:
            continue
        if lower in alias_map:
            continue
        if lower in schema_lower:
            continue
        if lower in column_aliases:
            continue
        if token == "*":
            continue

        matching_tables = [
            table
            for table in resolved_tables
            if _column_exists(token, schema[table])
        ]
        if not matching_tables and resolved_tables:
            return _column_error(token, resolved_tables[0], schema[resolved_tables[0]])
    return None


# _column_exists - check whether a column name exists case-insensitively
def _column_exists(column: str, columns: list[str]) -> bool:
    return column.lower() in {name.lower() for name in columns}


# _column_error - format a specific unknown-column validation error
def _column_error(column: str, table: str, columns: list[str]) -> str:
    available = ", ".join(columns)
    return (
        f"Column '{column}' does not exist in table '{table}'. "
        f"Available columns: {available}"
    )
