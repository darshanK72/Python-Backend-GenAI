# Gen AI & Data Science Notebooks

Structured learning library: **archived lessons**, **module recaps**, and **roadmaps** for backend & Gen AI.

## Start here

| Notebook | Purpose |
|----------|---------|
| **[`00-complete-syllabus.ipynb`](00-complete-syllabus.ipynb)** | Full syllabus, study order, progress tracker, lesson index |
| Each folder’s **`00-recap-*.ipynb`** | Quick recap + links to lessons in that topic |

## Folder structure

```
01. Notebooks/
├── 00-complete-syllabus.ipynb          ← open first
├── 01. AI Foundations/
├── 02. Python Fundamentals/
├── 03. Data Structures/
├── 04. NumPy and Algorithms/
├── 05. Pandas and Data Analysis/
├── 06. Data Visualization/
├── 07. Strings and Datetime/
├── 08. Probability and Statistics/
├── 09. Object-Oriented Programming/
├── 10. Graphs and Algorithms/
├── 11. References/
├── 12. Projects and Capstones/
├── 13. Python Backend (Planned)/       ← add Django/FastAPI notebooks here
└── 14. Generative AI Deep Dive (Planned)/  ← add LLM/RAG notebooks here
```

Each topic folder contains:

- **`00-recap-<topic>.ipynb`** — summary, cheat sheet, self-check questions
- **Lesson notebooks** — full Colab-style lessons (`# Lesson N`, `#### Task`, `# S1.1` exercises)

## How lesson notebooks are structured

1. Markdown title (`# Lesson N: Topic`)
2. `### Teacher-Student Tasks` — concepts and context
3. `#### Task 1, 2, …` — theory in chunks
4. Code cells tagged `# S1.1:`, `# S2.1:` — hands-on practice
5. Often uses public datasets (S3 URLs)

## Study workflow

1. Open **`00-complete-syllabus.ipynb`** and pick the next unchecked module.
2. Read that module’s **`00-recap`** (5 min preview).
3. Work through lesson notebooks in order inside the folder.
4. Re-read the recap before starting projects or the next module.

## Archive notes

- Lesson **29** (Tuples I) and **38** are missing from the original archive.
- **Projects** live in `12. Projects and Capstones/` (files `48`–`53`).
- Regenerate recap notebooks: `python _build_recap_notebooks.py` (optional).
