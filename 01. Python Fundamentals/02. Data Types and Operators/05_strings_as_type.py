# 05 — str type (basics; more in folder 04 Strings)
# Run: python 05_strings_as_type.py

# --- 1. Three ways to quote strings ---
s1 = "double quotes"
s2 = 'single quotes'
s3 = """multi-line
string"""
print(s1)
print(s2)
print(s3)

# --- 2. Embedding quotes ---
quote = "He said, \"Hello\""
apostrophe = "It's Python"
print(quote)
print(apostrophe)

# --- 3. String is a sequence of characters ---
word = "Python"
print("len(word) =", len(word))
print("word[0] =", word[0])       # indexing starts at 0
print("word[-1] =", word[-1])     # -1 = last character

# --- 4. Slicing [start:stop:step] — stop is exclusive ---
print("word[0:3] =", word[0:3])   # "Pyt"
print("word[::-1] =", word[::-1]) # reverse

# --- 5. Strings are immutable ---
# word[0] = "p"   # Uncomment -> TypeError

# --- 6. Common string operations ---
text = "  hello world  "
print("upper:", text.upper())
print("strip:", text.strip())
print("replace:", text.replace("world", "Python"))
print("'hello' in text:", "hello" in text.strip())

# --- 7. Concatenation and repetition ---
a = "Py"
b = "thon"
print(a + b)
print(a * 3)
