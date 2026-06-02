# 12 — Bitwise operators (work on integer bits)
# Run: python 12_bitwise_operators.py
#
# &  |  ^  ~  <<  >>
# Useful for flags, permissions, low-level math — less common in everyday scripts.

a = 12    # 1100 in binary
b = 10    # 1010 in binary

print("a =", a, "b =", b)
print("a & b =", a & b)    # AND — bit 1 only if both bits are 1
print("a | b =", a | b)    # OR
print("a ^ b =", a ^ b)    # XOR — 1 if bits differ
print("~a =", ~a)          # NOT — inverts bits (result follows two's complement)

print("a << 1 =", a << 1)  # left shift — multiply by 2
print("a >> 1 =", a >> 1)  # right shift — integer divide by 2

# --- Practical tiny example: even/odd with & 1 ---
n = 17
print(n, "is odd:", (n & 1) == 1)
