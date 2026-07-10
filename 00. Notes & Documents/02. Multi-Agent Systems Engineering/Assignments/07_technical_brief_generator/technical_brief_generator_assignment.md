# Assignment 07 — Technical Brief Generator

**Source:** MAS_TRAINING-003_Multi-Agent_Systems_Engineering (MAS Assignment 02)  
**Track:** Multi-Agent Systems Engineering  
**Difficulty:** Easy  
**Marks:** 10  
**Estimated time:** ~2.5 hours  
**Required stack:** Python · LangGraph · OpenAI · 3 nodes

---

## Pattern

Sequential / Prompt Chaining — with programmatic quality gate between stages

---

## Scenario

Engineering teams need well-researched technical briefs before making architecture decisions. Build a pipeline that turns a topic into a structured brief. A quality gate ensures the research is deep enough before the Writer runs — preventing superficial outputs without human review.

---

## What You Need to Build

Three nodes:

| Node | Responsibility |
|------|----------------|
| **Researcher** | Produces a numbered list of at least **7 distinct facts** about the topic. Facts must be specific (not vague generalisations). On a retry call, it receives the existing facts and must add new ones rather than repeating prior output. |
| **Analyst** | Reads the fact list and distils it into structured insights. Sets `claim_count` = the number of distinct, verifiable claims found. A valid claim is a specific factual statement with a subject and predicate, e.g. *'Microservices reduce deployment coupling.'* A vague statement like *'Microservices are useful'* does not count. |
| **Writer** | Only runs when `claim_count >= 5`. Produces a structured brief with three sections: **Overview** (1 paragraph, 80–100 words), **Key Considerations** (3–5 bullets, each a single sentence), and **Recommendation** (1 paragraph, 60–80 words stating the author's recommendation on the topic). |

### Quality gate behaviour

- If `claim_count < 5` **AND** `retry_count < 2` → route back to **Researcher**. Increment `retry_count`.
- If `claim_count < 5` **AND** `retry_count >= 2` → route to **Writer** anyway with a note: *'Research incomplete — only {n} claims found.'*
- State must visibly show `claim_count` and `retry_count` at each node transition in the console.
- The gate must be implemented as a **conditional edge** — not `if/else` inside a node.

### Test topics

| Topic | Purpose |
|-------|---------|
| 'Event-driven architecture' | Happy path — gate passes on first try |
| 'GraphQL vs REST APIs' | Design Researcher prompt such that this topic triggers at least one retry |

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — State Management** | Design the state schema: facts list, insights list, `claim_count`, `retry_count`, article. | 20 min |
| **M2 — Agent Implementation** | Build the Researcher and Analyst agents with prompts that produce structured, countable output. | 50 min |
| **M3 — Quality Gate** | Implement the gate as a conditional edge routing back to Researcher or forward to Writer. | 40 min |
| **M4 — Testing & Docs** | Test both topics; README shows the gate decision (`claim_count`, `retry_count`) in the state trace. | 30 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **Graph & Pattern** | Correct LangGraph StateGraph; correct sequential pattern with quality gate; all nodes and edges present | Framework present but pattern partially wrong or a node/edge missing | Wrong framework or pattern absent |
| 2 | **Quality Gate** | Conditional edge routes back to Researcher when `claim_count < 5`; `retry_count` increments; Writer only runs after gate passes or retry limit reached | Gate present but routing wrong; Writer runs even when it should retry | No gate; purely linear; Writer always runs |
| 3 | **State & Orchestration** | State flows cleanly through all nodes; context preserved; hand-offs correct | State partially lost between nodes; context missing at 1+ point | Pipeline breaks; state not shared |
| 4 | **End-to-End Run** | Runs fully; passes all evaluator test cases; output matches spec | Minor error on 1 test case; mostly correct | Crashes or wrong output on sample |
| 5 | **Documentation** | PEP-8; README with setup + diagram + transcript; all data files committed | Code runs; README missing diagram or transcript | No README; no sample output; unreadable |

---

## Submission Checklist

- [ ] Gate implemented as a conditional edge function
- [ ] `claim_count` and `retry_count` printed at each node transition
- [ ] README shows at least one retry cycle
- [ ] Writer brief has Overview, Key Considerations, and Recommendation sections

---

## Pass context (MAS course)

MAS pass criteria: **60/100 overall**, with at least **25/50** across Assignments 06–10 and at least **25/50** across Assignments 11–15.
