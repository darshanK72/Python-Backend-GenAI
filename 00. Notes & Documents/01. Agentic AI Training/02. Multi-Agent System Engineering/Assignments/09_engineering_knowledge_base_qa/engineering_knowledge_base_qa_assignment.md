# Assignment 09 — Engineering Knowledge Base Q&A

**Source:** MAS_TRAINING-003_Multi-Agent_Systems_Engineering (MAS Assignment 04)  
**Track:** Multi-Agent Systems Engineering  
**Difficulty:** Medium  
**Marks:** 10  
**Estimated time:** ~3 hours  
**Required stack:** Python · LangGraph · FAISS · LangChain · OpenAI · wikipedia-api

---

## Pattern

Corrective RAG — Retrieve → Grade relevance → Generate with citation

---

## Scenario

Build an internal knowledge base assistant that answers engineering questions from a set of indexed articles. Unlike basic RAG, this agent grades retrieved documents for relevance before generating — ensuring answers are grounded and sources are cited. Questions outside the knowledge base return *'Insufficient information'* rather than a hallucinated answer.

---



## What You Need to Build



### Document corpus — use these 7 Wikipedia articles

Fetch articles using `wikipedia-api`:

```python
wiki = wikipediaapi.Wikipedia(language='en', user_agent='MAS-Training/1.0')
text = wiki.page('Software engineering').text
```


| #   | Wikipedia Article Title    | Topic Covered                                                  |
| --- | -------------------------- | -------------------------------------------------------------- |
| 1   | Software engineering       | Foundations, lifecycle, engineering disciplines                |
| 2   | Agile software development | Agile manifesto, Scrum, sprint ceremonies                      |
| 3   | Continuous integration     | CI pipelines, test automation, trunk-based development         |
| 4   | DevOps                     | DevOps culture, toolchain, DORA metrics                        |
| 5   | Technical debt             | Code quality, refactoring trade-offs, remediation strategies   |
| 6   | Microservices              | Service decomposition, inter-service communication, deployment |
| 7   | Test-driven development    | TDD cycle, test-first design, benefits and common objections   |




### Indexing

- Chunk each article into ~500-character segments with 50-character overlap.
- Add `doc_title` and `chunk_index` to metadata.
- Embed with `OpenAIEmbeddings` and index in **FAISS**.
- Save index to disk with `FAISS.save_local('faiss_index')`.
- Commit a **rebuild script** — no binary index in the repo.



### Three nodes


| Node          | Behaviour                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Retriever** | Runs `FAISS.similarity_search(query, k=4)` and writes the 4 retrieved chunks to `retrieved_docs` in state.                                                                                                                                                                                                                                                                                                                                      |
| **Grader**    | For each document in `retrieved_docs`, calls OpenAI with: *'Is the following text relevant to answering this question: {question}? Reply with only: relevant or irrelevant.'* Writes passing docs to `relevant_docs` and logs each decision in `grading_trace`.                                                                                                                                                                                 |
| **Generator** | Reads `relevant_docs`. **(1)** ≥2 relevant docs → answer in 2–4 sentences, cite all source documents by title at the end. Format: *'Sources: [Article Title 1], [Article Title 2]'*. **(2)** Exactly 1 relevant doc → answer with note: *'Note: only one source available — answer may be incomplete.'* **(3)** 0 relevant docs → return: *'Insufficient information in the knowledge base to answer this question.'* Do not attempt to answer. |




### Test queries


| Query                                                                 | Expected                                                |
| --------------------------------------------------------------------- | ------------------------------------------------------- |
| 'What is trunk-based development and why do teams adopt it?'          | In-scope (Continuous integration article)               |
| 'How does technical debt accumulate and how should teams address it?' | In-scope (Technical debt article)                       |
| 'What is the difference between microservices and a monolith?'        | In-scope                                                |
| 'What are the current interest rates set by the Federal Reserve?'     | Out-of-scope → must return *'Insufficient information'* |


---



## Milestones


| Phase                       | What you're building                                                                                           | Time   |
| --------------------------- | -------------------------------------------------------------------------------------------------------------- | ------ |
| **M1 — Document Ingestion** | Fetch all 7 articles, chunk, embed, and save FAISS index; include rebuild script.                              | 40 min |
| **M2 — Retrieval Pipeline** | Build retriever node (top-4 FAISS search) and grader node (binary relevance scoring per doc).                  | 50 min |
| **M3 — Answer Generation**  | Build generator node with the 3-tier response logic (≥2 / 1 / 0 relevant docs).                                | 40 min |
| **M4 — Evaluation & Docs**  | Run all 4 test queries; show grading trace in README; confirm out-of-scope returns 'Insufficient information'. | 30 min |


---



## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.


| #   | Criterion                 | 2 marks — Full                                                                                             | 1 mark — Partial                                                                   | 0 marks — Missing                                        |
| --- | ------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------- |
| 1   | **FAISS + Grader Setup**  | LangGraph + FAISS from Wikipedia docs; grader node filters irrelevant docs; 7 articles indexed             | Chroma substituted for FAISS (–1); or grader node always passes all docs           | No FAISS; no LangGraph; no grader                        |
| 2   | **Relevance Grading**     | Out-of-scope query returns 'Insufficient information'; ≥2-doc rule applied correctly on all 4 test queries | Grader present but out-of-scope answer still attempted; or citation format missing | No grader; all retrieved docs pass directly to generator |
| 3   | **State & Orchestration** | State flows cleanly through all nodes; context preserved; hand-offs correct                                | State partially lost between nodes; context missing at 1+ point                    | Pipeline breaks; state not shared                        |
| 4   | **End-to-End Run**        | Runs fully; passes all evaluator test cases; output matches spec                                           | Minor error on 1 test case; mostly correct                                         | Crashes or wrong output on sample                        |
| 5   | **Documentation**         | PEP-8; README with setup + diagram + transcript; all data files committed                                  | Code runs; README missing diagram or transcript                                    | No README; no sample output; unreadable                  |


---



## Submission Checklist

- [ ] FAISS rebuild script committed — no binary index
- [ ] Grading trace (relevant/irrelevant per doc) printed to console for each query
- [ ] All 4 test queries in README with expected vs actual output
- [ ] Out-of-scope query returns 'Insufficient information'

---



## Pass context (MAS course)

MAS pass criteria: **60/100 overall**, with at least **25/50** across Assignments 06–10 and at least **25/50** across Assignments 11–15.