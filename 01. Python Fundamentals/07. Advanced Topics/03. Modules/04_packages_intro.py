# 04 — Packages (folders with __init__.py)
# Run: python 04_packages_intro.py
#
# package/
#   __init__.py
#   module_a.py
#   module_b.py
#
# import package.module_a
#
# pip install requests  — third-party packages (outside stdlib)
# python -m venv .venv  — virtual environment (isolate dependencies)

print("Packages group related modules in a directory.")
print("Use venv + pip for real projects with external libraries.")
print("stdlib docs: https://docs.python.org/3/library/")

# --- Example: namespace package concept ---
# If you create mypkg/__init__.py and mypkg/utils.py you can:
# from mypkg.utils import something
