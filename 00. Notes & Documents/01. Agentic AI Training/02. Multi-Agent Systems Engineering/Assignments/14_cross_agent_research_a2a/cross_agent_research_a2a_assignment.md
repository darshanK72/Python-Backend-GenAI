# Assignment 14 — Cross-Agent Research via A2A Protocol

**Source:** MAS_TRAINING-003_Multi-Agent_Systems_Engineering (MAS Assignment 09)  
**Track:** Multi-Agent Systems Engineering  
**Difficulty:** Hard  
**Marks:** 10  
**Estimated time:** ~3 hours  
**Required stack:** Python · FastAPI · httpx · LangGraph · OpenAI

---

## Pattern

A2A Protocol — two independent agent services communicate via HTTP following the A2A spec

---

## Scenario

MCP connects one agent to tools. A2A connects one agent to another autonomous agent. Build two independent services that collaborate via the A2A protocol: a ResearchAgent that runs as an A2A server and a WriterAgent that discovers it, delegates a research task, and writes a 300-word brief from the results. The goal is to understand the A2A handshake — discovery via AgentCard, task delegation, and result retrieval.

Both services run locally (ports **8001** and **8002**). No cloud deployment needed. The A2A calls between them must be visible in server logs.

---

## What You Need to Build

### A2A endpoints on ResearchAgent (port 8001)

| Endpoint | Method | Details |
|----------|--------|---------|
| `/.well-known/agent.json` | GET | Returns an AgentCard JSON with: `name`, `version` (1.0), `description`, `url` (`http://localhost:8001`), and `skills` array. Each skill must have: `name`, `description`, `inputSchema` (`{type: object, properties: {topic: {type: string}}}`), and `outputSchema` (`{type: object, properties: {output: {type: string}}}`). |
| `/tasks/send` | POST | Accepts: `{id: str, message: {role: 'user', content: str}}`. Calls OpenAI to research the topic. Returns: `{id: str, status: 'completed', output: str}`. |
| `/tasks/{task_id}` | GET | Returns the same TaskResult as `/tasks/send` for the given `task_id` (async polling pattern). |

ResearchAgent OpenAI prompt for `/tasks/send` must produce structured research:

> *'3 Key Facts: [numbered list]. 2 Current Trends: [numbered list]. 1 Notable Challenge: [sentence].'*

Log every incoming request: *'A2A task received: {task_id} — topic: {content}'*

### WriterAgent (LangGraph, port 8002) — 3 nodes

| Node | Behaviour |
|------|-----------|
| **discovery_node** | Calls `GET http://localhost:8001/.well-known/agent.json` via httpx. Parses the AgentCard and logs: *'Agent discovered: {name} v{version} — Skills: {skill names}'*. Writes AgentCard to state. |
| **delegation_node** | Constructs a Task payload: `{id: str(uuid4()), message: {role: 'user', content: topic}}`. POSTs to `/tasks/send`. Reads the TaskResult output string and writes it to `research_result` in state. Logs: *'A2A task {id} completed. Research received ({n} characters).'* |
| **writer_node** | Receives `research_result`. Calls OpenAI to write a 300-word brief structured as: Introduction (60–80 words), Main Body (2 paragraphs, each referencing at least 1 fact from the research), and Conclusion (60–80 words). |

### README — A2A vs MCP comparison (100+ words covering these 4 points)

- **Who initiates:** In MCP, the agent calls tools. In A2A, agents call other agents — each side has its own reasoning loop.
- **Discovery:** A2A requires fetching an AgentCard first to understand capabilities. MCP uses a tool registry.
- **Coupling:** A2A agents are independent services; they can be written in different languages and deployed separately. MCP tools are registered with a single agent's server.
- **When to use each:** MCP for integrating tools and data sources into one agent. A2A for delegating reasoning tasks to another agent that has specialised capabilities or data access.

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — Research Agent Server** | Build ResearchAgent with all 3 A2A endpoints; confirm AgentCard returns valid JSON and `/tasks/send` calls OpenAI. | 40 min |
| **M2 — Agent Discovery** | Implement `discovery_node` in WriterAgent: fetches and parses AgentCard before any delegation. | 50 min |
| **M3 — Task Delegation & Writing** | Build `delegation_node` (POST to A2A), `writer_node` (article from research), and wire into StateGraph. | 40 min |
| **M4 — Live Integration & Docs** | Run both services simultaneously; demo 2 topics; capture A2A server logs; write README comparison. | 30 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **A2A Implementation** | All 3 endpoints correct on ResearchAgent; WriterAgent calls AgentCard + `/tasks/send` via httpx; A2A calls visible in ResearchAgent logs | One endpoint missing or wrong schema; httpx calls made but response not parsed correctly | A2A not implemented; agents communicate via Python imports instead of HTTP |
| 2 | **Agent Discovery** | `discovery_node` fetches and parses AgentCard; logs show the discovered agent name and skills; delegation uses the discovered endpoint URL | AgentCard fetched but not logged or not used to confirm capabilities before delegating | No discovery step; WriterAgent hardcodes everything without AgentCard lookup |
| 3 | **State & Orchestration** | State flows cleanly through all nodes; context preserved; hand-offs correct | State partially lost between nodes; context missing at 1+ point | Pipeline breaks; state not shared |
| 4 | **End-to-End Trace** | Both services start independently; A2A HTTP calls logged for 2 topics; article references facts from the research output | One service fails or A2A logs missing; article content is generic and doesn't reflect research | Cannot run both services simultaneously; A2A communication not demonstrated |
| 5 | **A2A vs MCP Comparison** | README has 100+ words covering all 4 specified comparison points; PEP-8 code; diagram of 2-service architecture | Comparison < 100 words or covers fewer than 3 points; code runs | No comparison; README missing |

---

## Submission Checklist

- [ ] `research_agent.py` and `writer_agent.py` as separate files
- [ ] README: 2 start commands and example A2A log output
- [ ] A2A vs MCP comparison covering all 4 specified points
- [ ] Article in README explicitly references facts from the research output

---

## Pass context (MAS course)

MAS pass criteria: **60/100 overall**, with at least **25/50** across Assignments 06–10 and at least **25/50** across Assignments 11–15.
