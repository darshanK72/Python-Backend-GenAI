# 02 — re (regular expressions)
# Run: python 02_regex.py

import re

text = "Contact: darshan@example.com or support@site.org"

# --- 1. search — first match ---
match = re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
if match:
    print("email:", match.group())

# --- 2. findall — all matches ---
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
print("all emails:", emails)

# --- 3. sub — replace ---
censored = re.sub(r"@\w+", "@***", text)
print("censored:", censored)

# --- 4. split ---
parts = re.split(r"\s+or\s+", text)
print("split:", parts)

# --- 5. compile for reuse ---
phone_pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
print(phone_pattern.findall("Call 555-123-4567 or 555-999-8888"))
