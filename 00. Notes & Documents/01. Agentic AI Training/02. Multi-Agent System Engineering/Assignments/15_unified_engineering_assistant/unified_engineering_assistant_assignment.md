# Assignment 15 — Unified Engineering Assistant (Capstone)

**Source:** MAS_TRAINING-003_Multi-Agent_Systems_Engineering (MAS Assignment 10)  
**Track:** Multi-Agent Systems Engineering  
**Difficulty:** Hard  
**Marks:** 10  
**Estimated time:** ~3 hours  
**Required stack:** Python · LangGraph · FAISS · FastMCP · SQLite · MemorySaver · OpenAI

---

## Pattern

Supervisor Capstone — routes to RAG, DB, and Memory workers; FastMCP + FAISS + MemorySaver integrated

---

## Scenario

An engineering team needs a single assistant that handles three different types of questions in one conversation — without the user choosing a mode. A Supervisor classifies each query and routes it to the right specialist: an RAG worker for knowledge-base questions, a database worker for project data queries, and a memory worker to recall what was asked earlier in the session. All specialists surface their capabilities through FastMCP. Session memory persists so the assistant can recall prior queries when asked.

**Reuse** your FAISS index from Assignment 09 and your SQLite database from Assignment 10. Run your FAISS rebuild script and `seed_db.py` before testing — the evaluator will do the same.

---

## What You Need to Build

### FastMCP server — 3 tools

| Tool | Signature | Description |
|------|-----------|-------------|
| `rag_search` | `(query: str) -> str` | Calls `FAISS.load_local('faiss_index').similarity_search(query, k=3)`. Returns the top 3 matching chunks formatted as: *'Result 1 (Source: {doc_title}): {chunk_text}\nResult 2 ...'* |
| `db_query` | `(question: str) -> str` | Runs a LangChain SQL agent against `project_management.db` and returns the plain-English answer string. |
| `get_session_history` | `(thread_id: str) -> str` | Reads from a `session_store` dict keyed by `thread_id`. Returns a formatted recap or *'No prior queries in this session'* if the thread is new. |

### Supervisor routing logic

| Route | Query type | Examples |
|-------|-----------|----------|
| `rag` | Engineering concepts, best practices, methodology, architecture patterns | 'What is trunk-based development?', 'How do microservices compare to a monolith?' |
| `db` | Project data: tasks, incidents, team members, story points, sprint status | 'Which tasks are blocked?', 'Who is assigned the most tasks?' |
| `memory` | Questions about the session itself | 'What have I asked you so far?', 'Can you recap our conversation?' |
| `FINISH` | Conversation complete signals | 'Done', 'Thanks', 'That's all' |

After each answer, the supervisor appends the query and which worker was used to session history — so subsequent 'memory' queries return accurate history.

### State schema

| Field | Type | Purpose |
|-------|------|---------|
| `messages` | list | Conversation history |
| `route` | str | `rag` \| `db` \| `memory` \| `FINISH` |
| `worker_result` | str | Last worker's output |
| `session_history` | list[dict] | Each entry: `{turn: int, query: str, worker: str, summary: str}` |

### Required 4-query test session

| Query | Expected route | Notes |
|-------|---------------|-------|
| 1 | `rag` | 'What is the difference between microservices and a monolith?' |
| 2 | `db` | 'Which of our tasks are currently blocked?' |
| 3 | `memory` | 'What have I asked you so far?' — must return a recap referencing queries 1 and 2 |
| 4 | ambiguous | 'Based on our conversation, are there DevOps best practices I should apply to the blocked tasks?' — document in README how your supervisor handles it |

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — Data & MCP Layer** | Rebuild FAISS index; run `seed_db.py`; build FastMCP server with all 3 tools; confirm each tool returns data before building the graph. | 40 min |
| **M2 — Specialist Worker Agents** | Build 3 worker nodes: RAG worker (calls `rag_search`), DB worker (calls `db_query`), Memory worker (calls `get_session_history`). | 50 min |
| **M3 — Supervisor & Memory** | Build supervisor routing with MemorySaver checkpointing; update `session_store` after each worker response. | 30 min |
| **M4 — Full Integration Testing** | Run all 4 test queries; confirm Query 3 recaps Queries 1 and 2; README with routing trace + full architecture diagram. | 40 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **Full Stack Integration** | FAISS + FastMCP + MemorySaver all present and functional; all 3 FastMCP tools return non-empty results; graph compiled with checkpointer | 2 of 3 tools working; one returns empty or fails | Only 1 tool functional; 2 of 3 required components absent |
| 2 | **Supervisor Routing** | All 4 test queries routed correctly (rag, db, memory, FINISH); ambiguous query handled and documented | 3 of 4 queries correctly routed; 1 mismatch | Routing broken; supervisor always picks the same worker |
| 3 | **Memory & Session History** | Query 3 returns a recap that accurately references Queries 1 and 2 with correct worker names; session persists across all 4 turns with the same `thread_id` | MemorySaver present but Query 3 recap is empty or inaccurate | No MemorySaver; no session history; each call starts fresh |
| 4 | **End-to-End Run** | Runs fully; passes all evaluator test cases; output matches spec | Minor error on 1 test case; mostly correct | Crashes or wrong output on sample |
| 5 | **Architecture Diagram** | Diagram shows all 5 components (FAISS, FastMCP, SQLite, LangGraph, MemorySaver) and how they connect; README covers setup for all 3 backends; 4-query trace included | Diagram missing one component; one backend setup step missing | No diagram; README missing backend setup |

---

## Submission Checklist

- [ ] FastMCP server with all 3 tools committed
- [ ] FAISS rebuild script + `seed_db.py` — evaluator sets up all data in 2 commands
- [ ] Query 3 response in README explicitly mentions Query 1 and Query 2 topics
- [ ] Full architecture diagram showing all 5 components
- [ ] `thread_id` used consistently across all 4 queries

---

## Pass context (MAS course)

MAS pass criteria: **60/100 overall**, with at least **25/50** across Assignments 06–10 and at least **25/50** across Assignments 11–15.
