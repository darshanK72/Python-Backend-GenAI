# 07 — Docstrings (document your functions)
# Run: python 07_docstrings.py
#
# First string right after def line is the docstring.
# Access with help() or __doc__.

def area_of_circle(radius):
  """Return area of a circle given radius."""
  return 3.14159 * radius ** 2

print(area_of_circle(5))
print(area_of_circle.__doc__)
help(area_of_circle)

def describe_student(name, age, city="Nashik"):
    """
    Print a one-line student summary.

    Parameters:
        name (str): Student name.
        age (int): Age in years.
        city (str): City name (default Nashik).
    """
    print(f"{name}, {age}, from {city}")

describe_student("Darshan", 25)
