# Assignment 06 — Developer Assist Agent

**Source:** MAS_TRAINING-003_Multi-Agent_Systems_Engineering (MAS Assignment 01)  
**Track:** Multi-Agent Systems Engineering  
**Difficulty:** Easy  
**Marks:** 10  
**Estimated time:** ~2.5 hours  
**Required stack:** Python · LangGraph · OpenAI · 3 tools

---

## Pattern

ReAct — Thought → Action → Observation loop until Final Answer

---

## Scenario

Build a development assistant for an engineering team. The agent must reason through Thought → Action → Observation cycles to answer developer queries, picking the right tool for each request and looping until it has a confident final answer. A safety guard prevents the loop from exceeding 6 iterations.

---

## What You Need to Build

Three tools:

| Tool | Signature | Description |
|------|-----------|-------------|
| `story_estimator` | `(description: str) -> str` | Takes a free-text feature description. Returns a story point estimate (1, 2, 3, 5, 8, or 13) with a 2-sentence rationale. Example: *'5 points — requires OAuth integration and session management; no new infrastructure needed.'* |
| `tech_stack_advisor` | `(requirements: str) -> str` | Takes a set of technical requirements. Returns 2–3 tool or framework recommendations, each with a single-sentence reason. |
| `doc_summariser` | `(text: str) -> str` | Takes a block of technical documentation (any length). Returns exactly 3 bullet points covering the most important information. Each bullet is one sentence. |

### Agent behaviour

- The LLM node generates a structured **Thought** (what it is reasoning about), then either an **Action + Action Input** (tool to call and its argument), or a **Final Answer** (when no more tools are needed).
- Every Thought, Action, Action Input, and Observation must be **printed to the console** so the reasoning trace is visible.
- Final Answer should directly address the original question, synthesising the tool results where multiple tools were called.
- If the agent has not reached a Final Answer after **6 tool calls**, it must stop and return the best answer it has so far — not loop indefinitely.

### Sample test queries

| Query | Expected tool(s) |
|-------|------------------|
| 'Estimate the effort for adding a CSV export feature to the admin dashboard' | `story_estimator` |
| 'What stack should I use to build a real-time notification system?' | `tech_stack_advisor` |
| 'Summarise this doc: [paste a few paragraphs from a LangGraph or FastAPI README]' | `doc_summariser` |
| 'I need to add OAuth login — what tech should I use and how much effort will it take?' | `story_estimator` and `tech_stack_advisor` in sequence |

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — State Management** | Define the state schema tracking each reasoning step, tool calls, observations, and the final answer. | 30 min |
| **M2 — Tool Development** | Build the 3 tool functions and a dispatcher that routes to the right tool based on the agent's action. | 45 min |
| **M3 — Reasoning Loop** | Connect the LLM reasoning node with conditional edges — tool call → dispatcher → back to LLM, or final answer → END. | 45 min |
| **M4 — Testing & Docs** | Run all 4 sample queries; capture full Thought/Action/Observation trace for each in README. | 30 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **Graph & Pattern** | Correct LangGraph StateGraph; correct ReAct pattern; all nodes and edges present | Framework present but pattern partially wrong or a node/edge missing | Wrong framework or pattern absent |
| 2 | **ReAct Loop** | Thought → Action → Observation cycle visible for all 4 evaluator queries; different tools used for different inputs; 6-iteration guard present | Loop partially visible; agent uses the same tool regardless of input | No loop; agent answers in one pass without tool use |
| 3 | **State & Orchestration** | State flows cleanly through all nodes; context preserved; hand-offs correct | State partially lost between nodes; context missing at 1+ point | Pipeline breaks; state not shared |
| 4 | **End-to-End Run** | Runs fully; passes all evaluator test cases; output matches spec | Minor error on 1 test case; mostly correct | Crashes or wrong output on sample |
| 5 | **Documentation** | PEP-8; README with setup + diagram + transcript; all data files committed | Code runs; README missing diagram or transcript | No README; no sample output; unreadable |

---

## Submission Checklist

- [ ] All 3 tools return correctly formatted outputs as specified
- [ ] Iteration guard present and tested
- [ ] README transcript shows Thought/Action/Observation for each of the 4 sample queries
- [ ] LangGraph StateGraph with TypedDict state at module top
- [ ] `OPENAI_API_KEY` loaded from `.env` — never committed

---

## Pass context (MAS course)

MAS pass criteria: **60/100 overall**, with at least **25/50** across Assignments 06–10 and at least **25/50** across Assignments 11–15.
