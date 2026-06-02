# 01 — print() function
# Run: python 01_print.py
#
# print() sends text to the screen (standard output).
# Strings go in quotes: "double" or 'single' — both work the same here.

# --- 1. Simple message ---
# By default, print() adds a newline at the end (cursor moves to next line).
print("Hello, World!")

# --- 2. Multiple values ---
# You can pass several items; print() puts a SPACE between them by default.
print("Python", "is", "fun")

# --- 3. Blank line ---
# Calling print() with nothing prints one empty line.
print()
print("Above this line there was a blank line.")

# --- 4. sep — separator between values ---
# sep changes what goes BETWEEN arguments (default is a single space).
print("apple", "banana", "cherry", sep=" | ")

# --- 5. end — what to print at the end ---
# Default end is "\n" (newline). Change it to keep printing on the same line.
print("Loading", end="...")
print(" done!")  # continues on same line because previous print had no newline

# sep and end can be used together
print("2026", "06", "02", sep="-", end=" (date)\n")

# --- 6. Escape characters inside strings ---
# Backslash + letter = special character in the string.
print("Line one\nLine two")       # \n = new line
print("Tab\there")                # \t = tab (wider spacing)
print("Quote: \"Hello\"")         # \" = double quote inside "..."
print("It\'s fine")               # \' = apostrophe inside '...' (optional with "...")

# To print a real backslash, write \\ 
print("Path: C:\\Users\\Darshan")

# --- 7. + vs comma in print ---
# + joins strings only (both sides must be strings).
print("Hello" + " " + "World")

# Comma is easier when mixing text and numbers — print converts numbers to text.
score = 95
print("Your score is", score)     # comma adds space automatically
# print("Score: " + score)        # Uncomment → TypeError (can't add str + int)

# --- 8. Single-line vs multi-line string ---
# Triple quotes """ ... """ can span multiple lines (useful for paragraphs).
print(
    """Python is easy to read.
You can write code across multiple lines
inside one string like this."""
)
