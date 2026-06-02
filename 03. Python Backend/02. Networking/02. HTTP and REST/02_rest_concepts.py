# 02 — REST API concepts
# Run: python 02_rest_concepts.py

resources = [
    ("GET",    "/students",      "List all students"),
    ("GET",    "/students/101",  "Get student 101"),
    ("POST",   "/students",      "Create student (JSON body)"),
    ("PUT",    "/students/101",  "Replace student 101"),
    ("PATCH",  "/students/101",  "Partial update"),
    ("DELETE", "/students/101",  "Delete student 101"),
]

print("REST maps HTTP methods to resources:\n")
for method, path, desc in resources:
    print(f"  {method:6} {path:18} -> {desc}")
