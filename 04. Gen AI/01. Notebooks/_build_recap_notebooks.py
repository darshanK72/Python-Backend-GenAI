"""Generate 00 syllabus and module recap notebooks."""
import json
from pathlib import Path

ROOT = Path(__file__).parent

def md_cell(source: str):
    lines = source.strip().split("\n")
    return {"cell_type": "markdown", "metadata": {}, "source": [l + "\n" for l in lines]}

def code_cell(source: str):
    return {
        "cell_type": "code",
        "metadata": {},
        "source": [source + "\n"] if not source.endswith("\n") else [source],
        "outputs": [],
        "execution_count": None,
    }

def notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.11.0"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }

def write_nb(path: Path, cells):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notebook(cells), indent=1), encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")

# --- 00 Complete Syllabus ---
syllabus_md = r"""# 00 — Complete Syllabus & Learning Roadmap

Use this notebook as your **home base**. Open it whenever you want to recap, pick the next topic, or track progress.

---

## How archived lesson notebooks are built

Each lesson notebook (WhiteHat Jr / Colab style) typically follows this pattern:

| Section | Purpose |
|---------|---------|
| `# Lesson N: Topic` | Title and lesson number |
| `### Teacher-Student Tasks` | Concept intro, real-world context, images |
| `#### Task 1, 2, …` | Theory broken into small chunks |
| `# S1.1: …` code cells | Hands-on exercises (student tasks) |
| Datasets & URLs | Often loaded from public S3 buckets |

**How to study:** Read markdown → run code top-to-bottom → complete every `S*.*` exercise → use the module **recap** notebook (`00-recap-*.ipynb`) before moving on.

---

## Repository-wide learning path

| Phase | Location | Status |
|-------|----------|--------|
| 1 | `01. Python Fundamentals/` (`.py` scripts) | ✅ In repo |
| 2 | `02. Backend/` (MySQL, sockets, Django, FastAPI) | 🔶 Partial |
| 3 | `03. GUI/` (Tkinter) | ✅ Reference |
| 4 | **`04. Gen AI/01. Notebooks/`** (this tree) | ✅ Reorganized |

---

## Module map (open folder → start with `00-recap`)

| # | Module folder | Recap notebook | Lessons |
|---|---------------|----------------|---------|
| 01 | [01. AI Foundations](01.%20AI%20Foundations/) | `00-recap-ai-foundations.ipynb` | 2 |
| 02 | [02. Python Fundamentals](02.%20Python%20Fundamentals/) | `00-recap-python-fundamentals.ipynb` | 4 |
| 03 | [03. Data Structures](03.%20Data%20Structures/) | `00-recap-data-structures.ipynb` | 9 |
| 04 | [04. NumPy and Algorithms](04.%20NumPy%20and%20Algorithms/) | `00-recap-numpy-and-algorithms.ipynb` | 4 |
| 05 | [05. Pandas and Data Analysis](05.%20Pandas%20and%20Data%20Analysis/) | `00-recap-pandas-and-data-analysis.ipynb` | 7 |
| 06 | [06. Data Visualization](06.%20Data%20Visualization/) | `00-recap-data-visualization.ipynb` | 8 |
| 07 | [07. Strings and Datetime](07.%20Strings%20and%20Datetime/) | `00-recap-strings-and-datetime.ipynb` | 4 |
| 08 | [08. Probability and Statistics](08.%20Probability%20and%20Statistics/) | `00-recap-probability-and-statistics.ipynb` | 3 |
| 09 | [09. Object-Oriented Programming](09.%20Object-Oriented%20Programming/) | `00-recap-oop.ipynb` | 2 |
| 10 | [10. Graphs and Algorithms](10.%20Graphs%20and%20Algorithms/) | `00-recap-graphs-and-algorithms.ipynb` | 2 |
| 11 | [11. References](11.%20References/) | `00-recap-references.ipynb` | 2 |
| 12 | [12. Projects and Capstones](12.%20Projects%20and%20Capstones/) | `00-recap-projects-guide.ipynb` | 6 |
| 13 | [13. Python Backend (Planned)](13.%20Python%20Backend%20(Planned)/) | `00-roadmap-backend.ipynb` | *to build* |
| 14 | [14. Generative AI Deep Dive (Planned)](14.%20Generative%20AI%20Deep%20Dive%20(Planned)/) | `00-roadmap-gen-ai.ipynb` | *to build* |

---

## Recommended study order (full syllabus)

### Part A — Foundations
- [ ] **01 AI Foundations** → types of AI, industry applications
- [ ] **02 Python Fundamentals** → syntax, variables, loops, functions
- [ ] **03 Data Structures** → lists, dicts, tuples, comprehension

### Part B — Data science core
- [ ] **04 NumPy & Algorithms** → arrays, Shannon entropy
- [ ] **05 Pandas & Data Analysis** → Series, DataFrame, cleaning, time series, groupby
- [ ] **06 Data Visualization** → matplotlib, seaborn, folium
- [ ] **07 Strings & Datetime** → formatting, parsing, `datetime` module
- [ ] **08 Probability & Statistics** → discrete probability, correlation, OLS

### Part C — Software & graphs
- [ ] **09 OOP** → classes, encapsulation
- [ ] **10 Graphs & Algorithms** → graphs, Dijkstra, reference algorithms
- [ ] **11 References** → databases, Python ecosystem tools
- [ ] **12 Projects** → apply skills end-to-end

### Part D — Your roadmap (create notebooks here)
- [ ] **13 Backend** — Django REST, FastAPI, auth, PostgreSQL, deployment
- [ ] **14 Gen AI** — embeddings, RAG, LangChain/LlamaIndex, fine-tuning, eval, agents

---

## Archived lesson index (by filename)

### 01. AI Foundations
- `01-evolution-of-ai-and-types.ipynb` — ANI/AGI/ASI, history of AI
- `02-ai-applications-across-industries.ipynb` — healthcare, finance, IoT, etc.

### 02. Python Fundamentals
- `03-python-introduction.ipynb` — Colab, first programs
- `04-variables-and-data-types.ipynb`
- `05-mind-reader-game-loops-and-conditionals.ipynb`
- `06-python-functions.ipynb`

### 03. Data Structures
- `07`–`11` lists, nested lists, comprehension
- `26`–`28` dictionaries
- `30-python-tuples-ii.ipynb` *(Lesson 29 Tuples I not in archive)*

### 04. NumPy and Algorithms
- `12`–`15` NumPy arrays I & II
- `13`–`14` Claude Shannon algorithm I & II

### 05. Pandas and Data Analysis
- `16`–`17` Series, DataFrame
- `20`–`21` slicing, missing values
- `34` time series, `36` cleaning, `37` grouping & aggregation

### 06. Data Visualization
- `18` scatter/line (exoplanets), `19` box plots, `22` folium
- `23` count plots, `24` histograms, `25` annotated bars
- `39` bar plots, `41` pie & bell curve
- `40-correlation.ipynb` → also listed under **08** (statistics)

### 07. Strings and Datetime
- `31`–`33` string operations I–III
- `35-the-datetime-module.ipynb`

### 08. Probability and Statistics
- `42-discrete-probability.ipynb`
- `40-correlation.ipynb`
- `54-ordinary-least-squares.ipynb`

### 09. OOP
- `45-oop-classes-and-objects.ipynb`
- `47-oop-encapsulation-i.ipynb`

### 10. Graphs and Algorithms
- `68-graphs-and-dijkstras-algorithm.ipynb`
- `77-graph-algorithms-reference.ipynb`

### 11. References
- `78-database-fundamentals-reference.ipynb`
- `80-popular-tools-and-python-packages-reference.ipynb`

### 12. Projects and Capstones
- `48` string operations project
- `49` strings + datetime project
- `50` video game sales capstone (grouping)
- `51` custom plots + RNA complement
- `52` IoT time series capstone
- `53` air quality correlation project

---

## Gaps in archive (build or skip)

| Missing | Suggestion |
|---------|------------|
| Lesson 29 — Python Tuples I | Read `30-python-tuples-ii.ipynb` intro; practice tuple basics |
| Lesson 38 | Not in archive — continue to bar plots (`39`) |
| Lessons 43–44, 46, 48–53 (class) | Covered partly by projects folder |
| Gen AI depth | Use **14. Generative AI Deep Dive (Planned)** |
| Django / FastAPI | Use **13. Python Backend (Planned)** + `02. Backend/` code |

---

## Progress tracker

Copy this into your notes and check off modules:

```
[ ] 01 AI Foundations    [ ] 05 Pandas        [ ] 09 OOP
[ ] 02 Python Basics     [ ] 06 Visualization [ ] 10 Graphs
[ ] 03 Data Structures   [ ] 07 Strings       [ ] 11 References
[ ] 04 NumPy             [ ] 08 Statistics    [ ] 12 Projects
[ ] 13 Backend (planned) [ ] 14 Gen AI (planned)
```
"""

write_nb(ROOT / "00-complete-syllabus.ipynb", [md_cell(syllabus_md)])

# Module recap templates
MODULES = [
    (
        "01. AI Foundations",
        "00-recap-ai-foundations.ipynb",
        "AI Foundations",
        [
            ("01-evolution-of-ai-and-types.ipynb", "Evolution of AI; ANI vs AGI vs ASI; narrow vs general intelligence"),
            ("02-ai-applications-across-industries.ipynb", "AI in healthcare, finance, retail, IoT, education"),
        ],
        """**Recap questions**
1. Define AI in one sentence.
2. Name three types of AI by capability.
3. Give two examples of AI you use daily without noticing.""",
        None,
    ),
    (
        "02. Python Fundamentals",
        "00-recap-python-fundamentals.ipynb",
        "Python Fundamentals",
        [
            ("03-python-introduction.ipynb", "Colab, notebooks, `print`, basic I/O"),
            ("04-variables-and-data-types.ipynb", "int, float, str, bool; casting"),
            ("05-mind-reader-game-loops-and-conditionals.ipynb", "`while`, `if`/`elif`/`else`, mind reader game"),
            ("06-python-functions.ipynb", "`def`, parameters, return, scope"),
        ],
        """**Recap questions**
1. Difference between `=` and `==`?
2. When use `while` vs `for`?
3. Write a function that returns the max of two numbers.""",
        """# Quick reference
name = "Darshan"
age = 25
if age >= 18:
    print("Adult")
for i in range(3):
    print(i)
def greet(name):
    return f"Hello, {name}"
""",
    ),
    (
        "03. Data Structures",
        "00-recap-data-structures.ipynb",
        "Data Structures",
        [
            ("07-python-lists-i.ipynb", "Create, index, slice lists"),
            ("08-python-lists-ii.ipynb", "`count`, `index`, list methods"),
            ("09-python-lists-iii.ipynb", "More list operations"),
            ("10-nested-python-lists.ipynb", "2D lists, nested access"),
            ("11-list-comprehension.ipynb", "List comprehensions [x for x in ...]"),
            ("26-python-dictionary-i.ipynb", "Dict keys/values, access"),
            ("27-python-dictionary-ii.ipynb", "Dict methods, iteration"),
            ("28-python-dictionary-iii.ipynb", "Advanced dict usage"),
            ("30-python-tuples-ii.ipynb", "Tuple concat, unpack, `enumerate`, `zip`"),
        ],
        """**Recap questions**
1. List vs tuple — mutability?
2. Write a list comprehension for squares 1–5.
3. How do you get all keys from a dict?""",
        """# Quick reference
nums = [1, 2, 3]
nums.append(4)
d = {"a": 1, "b": 2}
squares = [x**2 for x in range(5)]
t = (1, 2, 3)
a, b, c = t
""",
    ),
    (
        "04. NumPy and Algorithms",
        "00-recap-numpy-and-algorithms.ipynb",
        "NumPy and Algorithms",
        [
            ("12-numpy-arrays-i.ipynb", "ndarray, shape, indexing"),
            ("13-claude-shannon-algorithm-i.ipynb", "Entropy, information theory intro"),
            ("14-claude-shannon-algorithm-ii.ipynb", "Shannon algorithm applications"),
            ("15-numpy-arrays-ii.ipynb", "Vectorized ops, broadcasting"),
        ],
        """**Recap questions**
1. Why NumPy vs Python lists for numeric data?
2. What is entropy in one line?
3. Shape of `np.zeros((3,4))`?""",
        """import numpy as np
arr = np.array([1, 2, 3])
print(arr.shape, arr.mean())
""",
    ),
    (
        "05. Pandas and Data Analysis",
        "00-recap-pandas-and-data-analysis.ipynb",
        "Pandas and Data Analysis",
        [
            ("16-pandas-series.ipynb", "Series creation, index, attributes"),
            ("17-pandas-dataframe.ipynb", "DataFrame, columns, head, info"),
            ("20-dataframe-slicing.ipynb", "`.loc`, `.iloc`, filtering"),
            ("21-treating-missing-values.ipynb", "`isna`, `fillna`, `dropna`"),
            ("34-time-series-data.ipynb", "Dates, `to_datetime`, extracting parts"),
            ("36-data-cleaning.ipynb", "Cleaning pipeline"),
            ("37-grouping-and-aggregation.ipynb", "`groupby`, `agg`"),
        ],
        """**Recap questions**
1. Series vs DataFrame?
2. `.loc` vs `.iloc`?
3. How to fill missing values with column median?""",
        """import pandas as pd
df = pd.read_csv("data.csv")
df.head()
df.isna().sum()
df.groupby("category")["sales"].mean()
""",
    ),
    (
        "06. Data Visualization",
        "00-recap-data-visualization.ipynb",
        "Data Visualization",
        [
            ("18-exoplanets-scatter-and-line-plots.ipynb", "Scatter, line plots (matplotlib)"),
            ("19-box-plots.ipynb", "Box plots, quartiles"),
            ("22-folium-maps.ipynb", "Interactive maps"),
            ("23-meteorite-landings-count-plots.ipynb", "Seaborn count plots"),
            ("24-histograms.ipynb", "Histograms, distributions"),
            ("25-annotated-bar-graphs.ipynb", "Bar charts with annotations"),
            ("39-bar-plots.ipynb", "Bar plots in depth"),
            ("41-pie-charts-and-bell-curve.ipynb", "Pie charts, normal distribution"),
        ],
        """**Recap questions**
1. When use histogram vs bar chart?
2. What does a box plot show?
3. Name two seaborn vs matplotlib differences.""",
        """import matplotlib.pyplot as plt
import seaborn as sns
plt.scatter(x, y)
sns.countplot(data=df, x="year")
""",
    ),
    (
        "07. Strings and Datetime",
        "00-recap-strings-and-datetime.ipynb",
        "Strings and Datetime",
        [
            ("31-string-operations-i.ipynb", "Indexing, slicing strings"),
            ("32-string-operations-ii.ipynb", "format(), placeholders"),
            ("33-string-operations-iii.ipynb", "Advanced string ops"),
            ("35-the-datetime-module.ipynb", "`datetime`, `strftime`, `strptime`"),
        ],
        """**Recap questions**
1. f-string vs `.format()`?
2. Parse `"2024-06-02"` to datetime?
3. Slice `"Python"[0:3]`?""",
        """from datetime import datetime
s = f"Today: {datetime.now():%Y-%m-%d}"
dt = datetime.strptime("2024-01-15", "%Y-%m-%d")
""",
    ),
    (
        "08. Probability and Statistics",
        "00-recap-probability-and-statistics.ipynb",
        "Probability and Statistics",
        [
            ("42-discrete-probability.ipynb", "Probability, binomial distribution"),
            ("40-correlation.ipynb", "Correlation, coefficient, causation vs correlation"),
            ("54-ordinary-least-squares.ipynb", "Linear regression, OLS"),
        ],
        """**Recap questions**
1. Correlation vs causation?
2. What does r close to -1 mean?
3. Purpose of OLS?""",
        None,
    ),
    (
        "09. Object-Oriented Programming",
        "00-recap-oop.ipynb",
        "Object-Oriented Programming",
        [
            ("45-oop-classes-and-objects.ipynb", "Classes, `__init__`, methods, objects"),
            ("47-oop-encapsulation-i.ipynb", "Encapsulation, private attributes"),
        ],
        """**Recap questions**
1. Class vs instance?
2. Purpose of `self`?
3. What is encapsulation?""",
        """class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hi, {self.name}"
""",
    ),
    (
        "10. Graphs and Algorithms",
        "00-recap-graphs-and-algorithms.ipynb",
        "Graphs and Algorithms",
        [
            ("68-graphs-and-dijkstras-algorithm.ipynb", "Graph representation, Dijkstra shortest path"),
            ("77-graph-algorithms-reference.ipynb", "BFS, DFS, reference algorithms"),
        ],
        """**Recap questions**
1. Directed vs undirected graph?
2. When use Dijkstra?
3. BFS vs DFS — one use case each?""",
        None,
    ),
    (
        "11. References",
        "00-recap-references.ipynb",
        "References (Quick Lookup)",
        [
            ("78-database-fundamentals-reference.ipynb", "SQL concepts, DB types, normalization"),
            ("80-popular-tools-and-python-packages-reference.ipynb", "NumPy, Pandas, sklearn, etc."),
        ],
        """Use these as **lookup sheets** — skim before interviews or when starting a new stack.""",
        None,
    ),
    (
        "12. Projects and Capstones",
        "00-recap-projects-guide.ipynb",
        "Projects and Capstones",
        [
            ("48-project-string-operations.ipynb", "Capital split, date format"),
            ("49-project-string-operations-and-datetime.ipynb", "Words emphasised, Friday 13th"),
            ("50-capstone-video-game-sales-grouping-aggregation.ipynb", "Video game sales — groupby"),
            ("51-project-custom-plots-and-rna-complement.ipynb", "Custom line plots, RNA complement"),
            ("52-capstone-iot-devices-time-series-plots.ipynb", "IoT temperature time series"),
            ("53-project-air-quality-correlation.ipynb", "Correlation, heatmaps, air quality"),
        ],
        """**Before each project:** skim related module recaps (05, 06, 07, 08).

**After each project:** write 3 bullet points of what you learned.""",
        None,
    ),
]

for folder, recap_name, title, lessons, questions, code in MODULES:
    lesson_lines = "\n".join(f"- **[{f}]({f})** — {desc}" for f, desc in lessons)
    cells = [
        md_cell(f"# Recap — {title}\n\nOpen this notebook for a **fast review** before projects or interviews.\n\n---\n\n## Lessons in this module\n\n{lesson_lines}"),
        md_cell(questions),
    ]
    if code:
        cells.append(md_cell("## Code cheat sheet"))
        cells.append(code_cell(code.strip()))
    cells.append(md_cell("---\n\n**Next:** Open the next module's `00-recap` or return to [`00-complete-syllabus.ipynb`](../00-complete-syllabus.ipynb)."))
    write_nb(ROOT / folder / recap_name, cells)

# Planned roadmaps
write_nb(
    ROOT / "13. Python Backend (Planned)" / "00-roadmap-backend.ipynb",
    [
        md_cell("""# Roadmap — Python Backend (Planned)

Create lesson notebooks here as you learn. Suggested order:

1. **HTTP & REST** — methods, status codes, JSON
2. **FastAPI** — routes, Pydantic, dependency injection, OpenAPI
3. **Django** — models, admin, ORM, migrations
4. **Django REST Framework** — serializers, viewsets, permissions
5. **Databases** — PostgreSQL, SQLAlchemy/Alembic (see `02. Backend/01. Databases/`)
6. **Auth** — sessions, JWT, OAuth2 basics
7. **Testing** — pytest, TestClient
8. **Deployment** — Docker, env vars, Gunicorn/Uvicorn

**Code practice:** `02. Backend/` in repo root.

**Recap:** After each topic, add a cell summarizing key APIs you used."""),
    ],
)

write_nb(
    ROOT / "14. Generative AI Deep Dive (Planned)" / "00-roadmap-gen-ai.ipynb",
    [
        md_cell("""# Roadmap — Generative AI Deep Dive (Planned)

Build notebooks here after completing Parts A–C of the main syllabus.

## Suggested modules

| Order | Topic | Key ideas |
|-------|--------|-----------|
| 1 | LLM fundamentals | tokens, context window, temperature, top-p |
| 2 | Prompt engineering | system/user messages, few-shot, chain-of-thought |
| 3 | Embeddings & vector DBs | cosine similarity, Chroma/Pinecone/FAISS |
| 4 | RAG | chunking, retrieval, grounding, eval |
| 5 | LangChain / LlamaIndex | chains, agents, tools |
| 6 | Fine-tuning & adapters | LoRA, when to fine-tune vs RAG |
| 7 | Evaluation & safety | hallucination, bias, guardrails |
| 8 | Production | APIs, caching, cost, observability |

**Prerequisites:** Modules 01–12, plus backend roadmap.

**Enable packages:** root `requirements.txt` (Gen AI section)."""),
    ],
)

print("Done.")
