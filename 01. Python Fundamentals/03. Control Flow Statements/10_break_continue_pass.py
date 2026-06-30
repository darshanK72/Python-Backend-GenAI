# 10 — break, continue, and pass
# Run: python 10_break_continue_pass.py

# --- 1. break — exit the loop immediately ---
for i in range(1, 11):
    if i == 6:
        break
    print(i, end=" ")
print("\nStopped at 6")

# --- 2. continue — skip rest of this iteration, go to next ---
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("\nOdd numbers only")

# --- 3. pass — placeholder (do nothing) ---
for i in range(5):
  pass   # TODO: implement later

if 10 > 5:
    pass   # valid empty block

# --- 4. break in while ---
n = 1
while n < 100:
    if n * n > 50:
        print("First n with n^2 > 50:", n)
        break
    n += 1

# --- 5. break only breaks innermost loop ---
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j, end="  ")
    print()
