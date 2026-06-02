# 01 — datetime (dates and times)
# Run: python 01_datetime.py

from datetime import datetime, date, time, timedelta

# --- 1. Now and today ---
now = datetime.now()
today = date.today()
print("now:", now)
print("today:", today)

# --- 2. Format strings ---
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%d/%m/%Y"))

# --- 3. Parse from string ---
parsed = datetime.strptime("2026-06-02 14:30", "%Y-%m-%d %H:%M")
print("parsed:", parsed)

# --- 4. timedelta (add/subtract days) ---
deadline = today + timedelta(days=30)
print("deadline:", deadline)
print("days until deadline:", (deadline - today).days)

# --- 5. time only ---
t = time(9, 30, 0)
print("time:", t)
