# Assignment 10 — Data Analytics Query Agent

**Source:** MAS_TRAINING-003_Multi-Agent_Systems_Engineering (MAS Assignment 05)  
**Track:** Multi-Agent Systems Engineering  
**Difficulty:** Medium  
**Marks:** 10  
**Estimated time:** ~2.5 hours  
**Required stack:** Python · LangGraph · LangChain SQL · SQLite · OpenAI

---

## Pattern

Reflection — SQL Generator writes a query; Validator critiques; loop retries on failure

---

## Scenario

Engineers and managers need instant answers from project data without writing SQL. Build a natural-language analytics agent that generates SQL, validates it for correctness and safety before running it, and returns a plain-English answer. The validator's feedback is passed back to the generator so it can self-correct — the agent never executes unvalidated SQL.

---

## What You Need to Build

### Database schema — create this

Include `seed_db.py` in your repo. Evaluators recreate the database with: `python seed_db.py`

Seed with: **3 projects**, **8 tasks** (mixed statuses), **4 team members**, **3 incidents** (1 critical, 1 high, 1 low).

```sql
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT CHECK(status IN ('planning','active','on_hold','completed','cancelled')),
    priority TEXT CHECK(priority IN ('low','medium','high','critical')),
    start_date DATE, due_date DATE, team_lead TEXT, budget_usd INTEGER
);
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT, project_id INTEGER REFERENCES projects(id),
    title TEXT NOT NULL,
    status TEXT CHECK(status IN ('todo','in_progress','review','done','blocked')),
    assignee TEXT, story_points INTEGER, due_date DATE
);
CREATE TABLE team_members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, role TEXT, department TEXT,
    email TEXT UNIQUE, hourly_rate INTEGER, skills TEXT
);
CREATE TABLE incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL,
    severity TEXT CHECK(severity IN ('critical','high','medium','low')),
    project_id INTEGER REFERENCES projects(id),
    reporter TEXT, assigned_to TEXT, description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Two nodes + a loop

| Node | Behaviour |
|------|-----------|
| **SQL Generator** | Receives the natural-language question + the DB schema (from `SQLDatabase.get_table_info()`). If this is a retry, it also receives the validator's error message. Produces a single **SELECT** SQL statement. Must never produce DDL or DML statements. |
| **SQL Validator** | Checks the generated SQL in order: (1) parse it with `sqlite3 EXPLAIN` — catch syntax errors; (2) scan for forbidden verbs: `DROP`, `DELETE`, `UPDATE`, `INSERT`, `ALTER`, `CREATE`; (3) verify every table name referenced exists in the schema; (4) verify every column name used exists in the correct table. If valid → route to executor. If invalid → return a specific error message. |

### Validator error message format

Error messages must be specific enough for the generator to fix them:

- *'Column \'assigneed\' does not exist in table \'tasks\'. Available columns: id, project_id, title, status, assignee, story_points, due_date'*
- *'Table \'employees\' does not exist. Available tables: projects, tasks, team_members, incidents'*
- *'SQL contains forbidden verb DELETE. Only SELECT statements are permitted'*

### Retry and termination

- Maximum **2 retries**. The validator's error message is passed to the generator on each retry.
- After 2 failed retries: return *'Unable to generate valid SQL after 2 attempts. Please rephrase your question.'*

### Final answer format

Each successful answer must contain 3 parts: (1) the validated SQL query displayed in a code block, (2) the raw result rows, (3) a plain-English summary sentence.

### Required test queries

| Type | Query | Expected SQL pattern |
|------|-------|-------------------|
| COUNT | 'How many tasks are currently blocked?' | `SELECT COUNT(*)` |
| JOIN | 'List all tasks along with the name of the team member assigned to each' | JOIN on tasks and team_members |
| FILTER | 'Show me all high or critical priority projects' | WHERE clause |
| AGGREGATE | 'What is the average story points per assignee?' | GROUP BY + AVG |

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — Database Setup** | Create and seed the SQLite database; verify with 2 manual queries; introspect schema using `SQLDatabase.get_table_info()`. | 20 min |
| **M2 — SQL Generation** | Build the SQL generator node — schema-aware, produces a SELECT query, accepts optional error feedback on retry. | 40 min |
| **M3 — Reflection Loop** | Build the validator node with all 4 checks, specific error messages, and retry routing. | 40 min |
| **M4 — Testing & Docs** | Run all 4 required query types; show at least 1 retry with validator error in README. | 30 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **Graph & Pattern** | Correct LangGraph StateGraph; correct reflection pattern; all nodes and edges present | Framework present but pattern partially wrong or a node/edge missing | Wrong framework or pattern absent |
| 2 | **Reflection Loop** | Validator rejects bad SQL with a specific error; generator uses error to revise; `retry_count` tracked; loop stops at max 2 retries | Validator present but error message is generic; generator retries without seeing the error | No validator; SQL executed without checks; no reflection loop |
| 3 | **SQL Accuracy** | Correct SQL for all 4 evaluator query types; schema introspection used | Correct for 3 of 4 types; 1 schema reference error | SQL consistently wrong; schema not used |
| 4 | **End-to-End Run** | Runs fully; passes all evaluator test cases; output matches spec | Minor error on 1 test case; mostly correct | Crashes or wrong output on sample |
| 5 | **Documentation** | PEP-8; README with setup + diagram + transcript; all data files committed | Code runs; README missing diagram or transcript | No README; no sample output; unreadable |

---

## Submission Checklist

- [ ] `seed_db.py` committed — evaluator recreates DB in one command
- [ ] Validator error messages are specific (name the bad column/table/verb)
- [ ] At least 1 retry cycle with error message visible in README
- [ ] Final answer shows SQL + raw result + plain-English summary

---

## Pass context (MAS course)

MAS pass criteria: **60/100 overall**, with at least **25/50** across Assignments 06–10 and at least **25/50** across Assignments 11–15.
