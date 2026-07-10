# Assignment 08 — Sprint Planning Assistant: Supervisor + FastMCP

**Source:** MAS_TRAINING-003_Multi-Agent_Systems_Engineering (MAS Assignment 03)  
**Track:** Multi-Agent Systems Engineering  
**Difficulty:** Medium  
**Marks:** 10  
**Estimated time:** ~3 hours  
**Required stack:** Python · LangGraph · FastMCP · OpenAI

---

## Pattern

Supervisor Agent — central LLM router dispatching to specialist workers via FastMCP

---

## Scenario

Engineering managers need a planning assistant that handles sprint questions without switching between tools. A Supervisor routes each request to the right specialist, which reads and writes sprint data through FastMCP. Workers never share a Python object directly — all state passes through the MCP server.

---

## What You Need to Build

### FastMCP server (start this before the graph)

The server holds a sprint backlog — a list of task objects in memory. Each task has: `title`, `assignee`, `story_points` (int), `status` (`'todo'` / `'in_progress'` / `'done'`), and `risk_level` (`'low'` / `'medium'` / `'high'`).

| Tool | Signature | Description |
|------|-----------|-------------|
| `get_backlog` | `() -> str` | Returns all tasks formatted as a readable list. Include story_points and status for each. |
| `add_task` | `(title, assignee, story_points) -> str` | Creates a new task with `status='todo'` and `risk_level='low'`. Returns `'Task added: {title} ({story_points} SP, assigned to {assignee})'`. |
| `check_capacity` | `(velocity: int = 40) -> str` | Sums story_points of all non-done tasks. Returns: `'Sprint is at {total}/{velocity} SP. {Over/Under} capacity by {n} SP.'` |
| `get_risk_summary` | `() -> str` | Returns tasks with `risk_level` `'high'` or `'medium'`, formatted as a numbered list. |

### Three worker nodes

| Worker | Behaviour |
|--------|-----------|
| **Sprint Builder** | Receives a feature description. Calls LLM to decompose it into 3–5 tasks. Calls `add_task` for each one. Returns a formatted summary: *'Created 4 tasks for [feature]: [task 1 (3 SP)], [task 2 (5 SP)], …'* |
| **Capacity Checker** | Calls `check_capacity`. Returns the formatted result plus a recommendation: *'Recommend descoping [task name]'* if over capacity, or *'Sprint has room for additional items'* if under. |
| **Risk Assessor** | Calls `get_backlog` and `get_risk_summary`. Uses LLM to identify 2–3 specific risks from the backlog. Each risk must name a specific task and explain why it is risky. |

### Supervisor routing logic

| User intent | Route to |
|-------------|----------|
| 'Plan [feature]' / 'Add tasks for…' / 'Break down…' | Sprint Builder |
| 'Check capacity' / 'How many SP' / 'Are we over budget' / 'Velocity' | Capacity Checker |
| 'Any risks' / 'What could go wrong' / 'Blockers' / 'Concerns' | Risk Assessor |
| 'Done' / 'That's all' / 'Nothing else' / 'Quit' | FINISH |

Tool calls must go through the **MCP protocol** (MCP client) — not direct Python imports.

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — MCP Server Build** | Build FastMCP server with all 4 tools; confirm server starts and tools are callable before building the graph. | 40 min |
| **M2 — Worker Agents** | Build 3 worker nodes, each calling FastMCP tools via MCP client and returning a formatted result to state. | 50 min |
| **M3 — Supervisor & Routing** | Build supervisor node with conditional routing to each worker and back; add FINISH condition. | 40 min |
| **M4 — Integration Testing** | Test 5 requests covering all 3 workers; README shows MCP tool call log and routing trace for each request. | 30 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **Supervisor + MCP Setup** | Correct LangGraph StateGraph; FastMCP server with all 4 tools; supervisor routes to all 3 workers via MCP client | Routes to 2 of 3 workers; one tool call bypasses MCP protocol | No supervisor routing; FastMCP absent; shared dict instead of MCP |
| 2 | **Core Functionality** | Primary technique fully working on evaluator's test cases; output matches spec | Works on sample but fails 1 of evaluator's 3 test cases | Core technique broken; no meaningful output |
| 3 | **Routing Loop** | Supervisor → worker → supervisor loop visible; results accumulate in state; FINISH correctly ends graph | Loop partially works; one worker doesn't route back to supervisor | No loop; linear execution only |
| 4 | **End-to-End Run** | Runs fully; passes all evaluator test cases; output matches spec | Minor error on 1 test case; mostly correct | Crashes or wrong output on sample |
| 5 | **Documentation** | PEP-8; README with setup + diagram + transcript; all data files committed | Code runs; README missing diagram or transcript | No README; no sample output; unreadable |

---

## Submission Checklist

- [ ] FastMCP server with all 4 tools committed
- [ ] Tool calls via MCP protocol — visible in logs
- [ ] README routing trace shows all 3 workers used
- [ ] Supervisor → worker → supervisor loop demonstrated

---

## Pass context (MAS course)

MAS pass criteria: **60/100 overall**, with at least **25/50** across Assignments 06–10 and at least **25/50** across Assignments 11–15.
