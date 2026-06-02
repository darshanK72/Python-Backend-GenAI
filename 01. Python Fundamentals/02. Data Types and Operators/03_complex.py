# 03 — Complex numbers
# Run: python 03_complex.py
#
# Form: real + imaginary*j   (j is used instead of math's i)

# --- 1. Creating complex values ---
c1 = 3 + 4j
c2 = complex(2, -1)    # same as 2 - 1j
print("c1 =", c1, type(c1))
print("c2 =", c2)

# --- 2. Accessing parts ---
print("c1.real =", c1.real)
print("c1.imag =", c1.imag)

# --- 3. Arithmetic ---
print("c1 + c2 =", c1 + c2)
print("c1 * c2 =", c1 * c2)
print("c1 ** 2 =", c1 ** 2)

# --- 4. conjugate and abs (magnitude) ---
print("c1.conjugate() =", c1.conjugate())
print("abs(c1) =", abs(c1))   # sqrt(3^2 + 4^2) = 5.0
