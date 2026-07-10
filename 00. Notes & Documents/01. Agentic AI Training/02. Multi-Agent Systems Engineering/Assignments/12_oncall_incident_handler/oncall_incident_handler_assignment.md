# Assignment 12 — On-Call Incident Handler

**Source:** MAS_TRAINING-003_Multi-Agent_Systems_Engineering (MAS Assignment 07)  
**Track:** Multi-Agent Systems Engineering  
**Difficulty:** Hard  
**Marks:** 10  
**Estimated time:** ~3 hours  
**Required stack:** Python · LangGraph · LangGraph MemorySaver · OpenAI

---

## Pattern

Nested Agents + Agentic Memory — escalation sub-graph + thread-scoped incident history

---

## Scenario

On-call engineers handle a stream of incidents during a shift and need an agent that remembers the shift's history, escalates critical issues through a deeper triage process, and spots patterns across related incidents. Build a two-level system: a main graph handles all incoming incidents, and a dedicated escalation sub-graph takes over for critical ones. Agentic memory persists all incidents from the session so the agent can cross-reference related events.

---

## What You Need to Build

### Sample incident files — commit to repo root

Create `incident_01.json`, `incident_02.json`, `incident_03.json`. Submit all 3 using the same `thread_id` to verify memory persistence across calls.

```json
{ "incident_id":"INC-001", "severity":"critical",
  "service":"payment-gateway", "error":"DB connection pool exhausted",
  "affected_users":2340, "region":"ap-south-1" }

{ "incident_id":"INC-002", "severity":"high",
  "service":"user-auth", "error":"JWT key rotation failed",
  "affected_users":450, "region":"us-east-1" }

{ "incident_id":"INC-003", "severity":"medium",
  "service":"payment-gateway", "error":"Elevated 503 rate post-recovery",
  "affected_users":210, "region":"ap-south-1" }
```

### Main graph — 4 nodes

| Node | Route | Behaviour |
|------|-------|-----------|
| **classifier_node** | All incidents | Reads the incident JSON. Extracts: `incident_id`, `severity`, `service`, `error`, `affected_users`. Classifies severity and routes accordingly. Before routing, appends a one-line summary to `incident_history`. |
| **response_node** | HIGH severity | Produces a direct response plan with exactly **3 immediate action steps** and an estimated time to resolution. |
| **log_node** | MEDIUM / LOW severity | Acknowledges the incident and adds it to a watch list. Prints: *'INC-003 logged for monitoring. No immediate action required. Added to watch list: payment-gateway elevated 503.'* |
| **notification_node** | All paths end here | Produces a 2-sentence summary of the action taken for the current incident. |

### Escalation sub-graph — 3 nodes (CRITICAL only)

Compiled separately as its own `StateGraph`, invoked for CRITICAL incidents only:

| Node | Output |
|------|--------|
| **root_cause_node** | Root cause hypothesis: *'Most likely cause: [1-sentence hypothesis]. Evidence: [2–3 bullet points referencing specific data from the incident].'* |
| **remediation_node** | Exactly **5 remediation steps** in priority order. Each step must include a time estimate in brackets and a concrete action. |
| **pagerduty_node** | Simulates a PagerDuty alert: *'🚨 PAGERDUTY ALERT | Incident: INC-001 | Severity: CRITICAL | Service: payment-gateway | Assigned to: [on-call from a hardcoded team roster of 3 names, round-robin] | Runbook: https://runbooks.internal/payment-gateway/p0'* |

### Agentic memory behaviour

- Compile the main graph with: `app = graph.compile(checkpointer=MemorySaver())`
- Call each incident with: `config = {'configurable': {'thread_id': 'shift-2024-11-15'}}`
- When INC-003 arrives (same service as INC-001), the classifier/response/log output must include a cross-reference: *'Note: This is the second payment-gateway incident this shift. INC-001 involved DB connection pool exhaustion — check if root cause is related.'*
- Cross-reference should only appear when the same service name is found in `incident_history`.

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — Agentic Memory Setup** | Configure MemorySaver with `thread_id`; verify that `incident_history` persists across 2 calls in the same thread. | 30 min |
| **M2 — Escalation Sub-graph** | Build the 3-node escalation sub-graph; compile it separately and test in isolation. | 50 min |
| **M3 — Main Graph & Routing** | Build classifier and all routing paths; integrate escalation sub-graph; add cross-reference logic. | 40 min |
| **M4 — Memory Integration Testing** | Submit all 3 incidents using the same `thread_id`; verify INC-003 references INC-001. | 40 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **Nested Sub-graph + Memory** | Escalation sub-graph compiled separately; MemorySaver configured; graph compiled with checkpointer; `thread_id` consistent across all 3 calls | Sub-graph not compiled separately; or MemorySaver not used as checkpointer | No nested sub-graph; no MemorySaver; sequential function calls used |
| 2 | **Agentic Memory** | INC-003 response references INC-001 by ID and service name from `incident_history`; history accumulates correctly across all 3 calls | MemorySaver present but INC-003 does not reference prior incidents | No memory; each call starts fresh |
| 3 | **Escalation Sub-graph Quality** | `root_cause_node` produces hypothesis with evidence; `remediation_node` produces 5 prioritised steps with time estimates; `pagerduty_node` prints formatted alert | One of the 3 sub-graph nodes produces generic output not referencing incident data | Escalation sub-graph not invoked for CRITICAL; or sub-graph is empty |
| 4 | **End-to-End Run** | Runs fully; passes all evaluator test cases; output matches spec | Minor error on 1 test case; mostly correct | Crashes or wrong output on sample |
| 5 | **Documentation** | PEP-8; README with setup + diagram + transcript; all data files committed | Code runs; README missing diagram or transcript | No README; no sample output; unreadable |

---

## Submission Checklist

- [ ] All 3 incident JSON files in repo root
- [ ] Escalation sub-graph as a separate StateGraph object (not inline logic)
- [ ] `thread_id = 'shift-2024-11-15'` in all 3 calls
- [ ] PagerDuty output shows correct format with round-robin roster
- [ ] README shows `incident_history` at each call and INC-003 cross-reference

---

## Pass context (MAS course)

MAS pass criteria: **60/100 overall**, with at least **25/50** across Assignments 06–10 and at least **25/50** across Assignments 11–15.
