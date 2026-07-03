# 02 — Python Libraries

**Hybrid learning:** notebooks for exploration and recap; `.py` scripts for terminal practice.

```bash
# repo root
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook "02. Python Libraries"
```

## Primary notebooks (start here)

| Folder | Notebook | Companion `.py` |
|--------|----------|-----------------|
| — | [00-recap-python-libraries.ipynb](00-recap-python-libraries.ipynb) | Index |
| 02. NumPy | [01-numpy.ipynb](02.%20NumPy/01-numpy.ipynb) | `01`–`08_*.py` |
| 03. Pandas | [01-pandas.ipynb](03.%20Pandas/01-pandas.ipynb) | `01`–`08_*.py` |
| 04. Matplotlib | [01-matplotlib.ipynb](04.%20Matplotlib/01-matplotlib.ipynb) | `01`–`04_*.py` (saves PNG) |
| 05. Seaborn | [01-seaborn.ipynb](05.%20Seaborn/01-seaborn.ipynb) | `01`–`03_*.py` |
| 09. Pillow | [01-pillow.ipynb](09.%20Pillow/01-pillow.ipynb) | `01`–`02_*.py` |
| 11. scikit-learn | [01-sklearn.ipynb](11.%20scikit-learn/01-sklearn.ipynb) | `01`–`03_*.py` |

## `.py` only (terminal / scripts)

| Folder | Topics |
|--------|--------|
| 01. Standard Library | datetime, re, collections, sqlite3, logging |
| 06. Requests | HTTP GET/POST (needs internet) |
| 07. BeautifulSoup | HTML parsing |
| 08. OpenPyXL | Excel |
| 10. Tkinter | Desktop GUI (needs a window) |
| 12. Pydentic | Pydantic validation, serializers, settings (`01`–`10_*.py`) |
| 13. Utilities | tqdm, dotenv, argparse |

Install everything from root [`requirements.txt`](../requirements.txt) (includes `jupyter`, `ipykernel`).
