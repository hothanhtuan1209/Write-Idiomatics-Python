"""
- Use if and else as a short ternary operator replacement.
- Python does not have the ternary operator (e.g. “x ? True : False”) that a number of other languages have.
"""

# Harmful solution
foo = True
value = 0

if foo:
    value = 1
print(value)


# Idiomatic solution
foo = True
value = 1 if foo else 0
print(value)
