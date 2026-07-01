# Python & Generative AI — Learning Repository

A structured workspace to relearn Python, build backend skills with **Flask**, **FastAPI**, and **Django**, then go deep into **Generative AI**.

## Learning path

| Phase | Folder | Focus |
|-------|--------|--------|
| 1 | [`01. Python Fundamentals/`](01.%20Python%20Fundamentals/) | Core Python — syntax, collections, functions, practice |
| 2 | [`02. Python Libraries/`](02.%20Python%20Libraries/) | NumPy, Pandas, Matplotlib, Requests, Tkinter, sklearn, and more |
| 3 | [`03. Python Backend/`](03.%20Python%20Backend/) | MySQL, networking, Flask, FastAPI, Django |
| 4 | [`04. Gen AI/`](04.%20Gen%20AI/) | LLMs, embeddings, RAG, LangChain, capstone API |

Work through folders **in order**. Each numbered subfolder in `01. Python Fundamentals` builds on the previous one.

## Quick start

```bash
# Create a virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate   # macOS/Linux

pip install -r requirements.txt

# Run any practice script, e.g.
python "01. Python Fundamentals/01. Getting Started/01_print.py"
```

## Repository layout

```
01. Python Fundamentals/     # Phase 1 — core Python (numbered lessons per folder)
02. Python Libraries/        # Phase 2 — NumPy, Pandas, APIs, GUI, ML intro
03. Python Backend/          # Phase 3 — databases, sockets, Flask, FastAPI, Django
04. Gen AI/01. Notebooks/    # Phase 4 — notebooks and Gen AI topics
```

## What’s next

1. **Refresh** — Run scripts in `01. Python Fundamentals` from `01. Getting Started` through `08. Practice Problems`.
2. **Backend** — Work through `03. Python Backend/` from SQLite through Flask, FastAPI, and Django.
3. **Gen AI** — Use `04. Gen AI/` for new notebooks and experiments; enable packages in `requirements.txt` when ready.

## Notes

- MySQL lessons use `.env` at repo root (see `03. Python Backend/config.example.env`).
- Older WhiteHat Jr lesson notebooks are archived under `04. Gen AI/01. Notebooks/` with topic-based filenames (e.g. `01-evolution-of-ai-and-types.ipynb`).
- MySQL examples assume a local server; adjust host/port/credentials in the scripts before running.
