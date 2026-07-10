# Assignment 13 — AI-Powered Delivery Team

**Source:** MAS_TRAINING-003_Multi-Agent_Systems_Engineering (MAS Assignment 08)  
**Track:** Multi-Agent Systems Engineering  
**Difficulty:** Hard  
**Marks:** 10  
**Estimated time:** ~3 hours  
**Required stack:** Python · AutoGen · OpenAI · 6 agents

---

## Pattern

Group Chat — AutoGen GroupChatManager; 5 role agents + 1 documentation writer

---

## Scenario

Simulate a software delivery team taking a feature from brief to deployment in an AutoGen group chat. Five specialist agents (Product Owner, Tech Lead, Developer, Tester, DevOps) work through the feature together, with each role contributing its domain expertise. A Documentation Writer produces a structured report at the end.

---

## What You Need to Build

### Feature to deliver

Use this feature request as the group chat kickoff:

> 'Add real-time task status notifications so that team members are instantly alerted via the app when any of their assigned tasks are updated.'

### Six agents — each must have a distinct `system_message`

| Agent | Responsibility |
|-------|----------------|
| **ProductOwner** | Writes 3–5 acceptance criteria in Given/When/Then format. Prioritises criteria by business value. Challenges the TechLead if the proposed design doesn't meet the criteria. |
| **TechLead** | Proposes the technical architecture: which components are needed, what technology stack (choose from: WebSockets / SSE / polling), and how data flows from a task update to the notification. Assigns the implementation to the Developer. Reviews the Developer's output before approving. |
| **Developer** | Writes the key function signatures and pseudocode for 2–3 core components: the WebSocket connection handler, the event publisher (triggered on task update), and the client subscription manager. Responds to TechLead's architecture review. |
| **Tester** | Defines 5 test cases: (1) happy path — user receives notification within 500ms, (2) concurrent connections — 100 users connected simultaneously, (3) reconnection — client recovers after disconnect, (4) authentication — unauthenticated users cannot subscribe, (5) message format validation — notification contains correct task_id, status, and timestamp. |
| **DevOps** | Describes the deployment configuration: Docker setup, port exposure, environment variables, and health check endpoint. When all other agents have confirmed their work is complete, outputs exactly: *'DEPLOYMENT_COMPLETE: Task Notifications v1.0 deployed to staging'*. |
| **DocumentationWriter** | Does **not** participate in the group chat. After the chat terminates, it receives the full transcript and produces a `delivery_report.md` with 5 sections: Executive Summary, Technical Design, Test Coverage, Deployment Configuration, and Open Questions. |

### Group chat configuration

- `max_round = 15`. Termination on `'DEPLOYMENT_COMPLETE'`. `speaker_selection_method = 'auto'`.
- Agents must reference each other by name when building on prior points — enforced in each agent's `system_message`: *'When building on another team member's input, reference their name explicitly.'*

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — Agent Design** | Write distinct `system_message` for all 6 agents; verify they produce different types of output in a short test run. | 30 min |
| **M2 — Group Chat Configuration** | Set up GroupChatManager with termination; run the full feature chat; tune prompts until all 5 role agents contribute meaningfully. | 50 min |
| **M3 — Documentation Agent** | Build the post-chat Documentation Writer; test with the transcript to confirm all 5 report sections are produced. | 40 min |
| **M4 — Full Simulation** | Run end-to-end; commit `transcript.txt` and `delivery_report.md`; README discusses group chat vs sequential. | 40 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **Group Chat Setup** | GroupChatManager with 6 distinctly prompted agents; termination on DEPLOYMENT_COMPLETE; all 6 agents contribute at least once | 5 agents contribute; termination condition missing or fires after 1 round | Fewer than 4 agents; sequential pattern used; no GroupChatManager |
| 2 | **Cross-Agent Collaboration** | Agents reference each other by name; TechLead responds to Developer output; Tester's test cases address the actual design proposed | 2–3 cross-references visible; some agents produce standalone outputs that ignore others | No cross-references; agents produce parallel independent outputs |
| 3 | **Delivery Report** | All 5 report sections present; content accurately reflects the group chat (not generic); test cases match the Tester agent's output | Report present but 1 section missing or doesn't reflect the actual chat | No delivery report; or report fabricated independently of transcript |
| 4 | **End-to-End Run** | Runs fully; passes all evaluator test cases; output matches spec | Minor error on 1 test case; mostly correct | Crashes or wrong output on sample |
| 5 | **Documentation** | PEP-8; README with setup + diagram + transcript; all data files committed | Code runs; README missing diagram or transcript | No README; no sample output; unreadable |

---

## Submission Checklist

- [ ] `transcript.txt` and `delivery_report.md` committed to repo
- [ ] All 6 agent `system_messages` are distinct and role-appropriate
- [ ] TechLead's architecture choices are visible in the Developer's and Tester's outputs
- [ ] README includes 150-word comparison of group chat vs sequential

---

## Pass context (MAS course)

MAS pass criteria: **60/100 overall**, with at least **25/50** across Assignments 06–10 and at least **25/50** across Assignments 11–15.
