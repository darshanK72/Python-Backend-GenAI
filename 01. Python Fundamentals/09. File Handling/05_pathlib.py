# 05 — pathlib (modern paths)
# Run: python 05_pathlib.py

from pathlib import Path

# --- 1. Current folder ---
here = Path(".")
print("cwd:", here.resolve())

# --- 2. Build paths with / ---
notes = here / "notes" / "readme.txt"
print("path object:", notes)

# --- 3. Create folder and file ---
folder = Path("demo_path")
folder.mkdir(exist_ok=True)

file = folder / "info.txt"
file.write_text("Hello from pathlib\n", encoding="utf-8")
print("exists:", file.exists())
print("read:", file.read_text(encoding="utf-8"))

# --- 4. List files ---
for item in folder.iterdir():
    print("item:", item.name)

# --- 5. Cleanup ---
file.unlink()
folder.rmdir()
print("cleaned up")
