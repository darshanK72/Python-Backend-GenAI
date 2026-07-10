# Assignment 11 — Feature Scoping Agent

**Source:** MAS_TRAINING-003_Multi-Agent_Systems_Engineering (MAS Assignment 06)  
**Track:** Multi-Agent Systems Engineering  
**Difficulty:** Medium  
**Marks:** 10  
**Estimated time:** ~3 hours  
**Required stack:** Python · LangGraph · OpenAI

---

## Pattern

Plan-and-Execute — Planner decomposes into structured steps; Executor iterates one step at a time

---

## Scenario

Before writing code, features need to be properly scoped: broken into work items with clear outputs and acceptance criteria. Build an agent that takes a feature request, decomposes it into an ordered delivery plan, then works through each step producing detailed specifications. A Reviewer assesses the complete output for delivery readiness.

---

## What You Need to Build

Three nodes:

| Node | Behaviour |
|------|-----------|
| **Planner** | Receives the feature request. Calls OpenAI (`temperature=0.7`) to produce a JSON array of **4–6 steps**. Each step must have 4 fields: `step_name` (short label), `description` (what this step covers), `expected_output` (specific deliverable), and `acceptance_criteria` (how you know the step is complete). On JSON parse error, retry once with a correction prompt. |
| **Executor** | Runs **one plan step per iteration** (uses `current_step_idx` to track position). For each step, calls OpenAI (`temperature=0.2`) and produces: a technical approach (2–3 sentences), any dependencies on prior steps or external systems, and an effort estimate (`small` = <4 hrs, `medium` = 4–8 hrs, `large` = >8 hrs). Appends `'Step {n}/{total}: {result}'` to `execution_log`. Increments `current_step_idx`. Routes back to itself until all steps are complete, then routes to Reviewer. |
| **Reviewer** | Reads the full `execution_log` and the original request. Produces a structured review with 3 fields: `coverage_score` (1–5), `gaps` (a list of missing concerns), and `recommendation` (either *'Approved for development'* or *'Needs revision: [specific changes required]'*). |

### Test features

| Feature | Description |
|---------|-------------|
| **Feature A** | 'Add email notifications when a task's status changes to blocked' |
| **Feature B** | 'Build a CSV export for the project backlog with filters by status and assignee' |

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — State & Graph Structure** | Define state: request, plan (list), `current_step_idx`, `execution_log` (list), review; build loop-capable graph skeleton. | 30 min |
| **M2 — Planner Implementation** | Build Planner with JSON plan output and parse error handling. | 50 min |
| **M3 — Execution Loop** | Implement Executor with per-step iteration; conditional edge: more steps → Executor, done → Reviewer. | 40 min |
| **M4 — Review & Docs** | Build Reviewer; run both test features; README includes plan JSON + full execution log. | 40 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **Graph & Pattern** | Correct LangGraph StateGraph; correct plan-and-execute pattern; all nodes and edges present | Framework present but pattern partially wrong or a node/edge missing | Wrong framework or pattern absent |
| 2 | **Plan Quality** | Plan JSON with all 4 required fields; 4–6 steps; logically sequenced; JSON parse error handled | JSON partial; 1–2 steps missing fields; no parse error handling | No JSON plan; prose output; Executor cannot iterate |
| 3 | **Execution Loop** | Executor iterates through every step; log accumulates all results; Reviewer only runs after all steps are done | Loop skips a step or Reviewer triggers early | No loop; all steps in one LLM call |
| 4 | **End-to-End Run** | Runs fully; passes all evaluator test cases; output matches spec | Minor error on 1 test case; mostly correct | Crashes or wrong output on sample |
| 5 | **Documentation** | PEP-8; README with setup + diagram + transcript; all data files committed | Code runs; README missing diagram or transcript | No README; no sample output; unreadable |

---

## Submission Checklist

- [ ] Plan JSON printed as formatted output
- [ ] Execution steps labelled (Step 1/5, Step 2/5, …) in console
- [ ] Reviewer output shows `coverage_score` + `gaps` + `recommendation`
- [ ] Both test features in README

---

## Pass context (MAS course)

MAS pass criteria: **60/100 overall**, with at least **25/50** across Assignments 06–10 and at least **25/50** across Assignments 11–15.
