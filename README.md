# Python & Generative AI — Learning Repository

A structured workspace to relearn Python, build backend skills with **Django** and **FastAPI**, then go deep into **Generative AI**.

## Learning path

| Phase | Folder | Focus |
|-------|--------|--------|
| 1 | [`01. Python Fundamentals/`](01.%20Python%20Fundamentals/) | Core Python — syntax, collections, functions, practice |
| 2 | [`02. Backend/`](02.%20Backend/) | MySQL, networking, then Django & FastAPI projects |
| 3 | [`03. GUI/`](03.%20GUI/) | Tkinter (optional / reference) |
| 4 | [`04. Gen AI/`](04.%20Gen%20AI/) | Notebooks and future Gen AI work |

Work through folders **in order**. Each numbered subfolder in `01. Python Fundamentals` builds on the previous one.

## Quick start

```bash
# Create a virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate   # macOS/Linux

pip install -r requirements.txt

# Run any practice script, e.g.
python "01. Python Fundamentals/01. Getting Started/first.py"
```

## Repository layout

```
01. Python Fundamentals/     # Phase 1 — relearn Python
02. Backend/
  ├── 03. Django/            # Django projects (add as you learn)
  ├── 04. FastAPI/           # FastAPI projects (add as you learn)
  ├── 01. Databases/01. MySQL/
  └── 02. Networking/01. Socket Programming/
03. GUI/01. Tkinter/         # Desktop GUI examples
04. Gen AI/01. Notebooks/    # Syllabus + topic folders + recap notebooks
```

## What’s next

1. **Refresh** — Run scripts in `01. Python Fundamentals` from `01. Getting Started` through `08. Practice Problems`.
2. **Backend** — Add small projects under `02. Backend/03. Django/` and `02. Backend/04. FastAPI/` as you follow tutorials.
3. **Gen AI** — Use `04. Gen AI/` for new notebooks and experiments; enable packages in `requirements.txt` when ready.

## Notes

- Root-level duplicate socket scripts were removed; canonical copies live in `02. Backend/02. Networking/01. Socket Programming/`.
- Older WhiteHat Jr lesson notebooks are archived under `04. Gen AI/01. Notebooks/` with topic-based filenames (e.g. `01-evolution-of-ai-and-types.ipynb`).
- MySQL examples assume a local server; adjust host/port/credentials in the scripts before running.
