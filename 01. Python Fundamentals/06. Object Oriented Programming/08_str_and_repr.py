# 08 — __str__ and __repr__
# Run: python 08_str_and_repr.py
#
# __str__  -> human-readable (print, str())
# __repr__ -> developer-friendly (debug, repr())

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.pages})"

b = Book("Python Basics", "Darshan", 300)
print(str(b))
print(repr(b))
print(b)   # print calls __str__ if available

# --- List shows repr ---
books = [b]
print(books)
