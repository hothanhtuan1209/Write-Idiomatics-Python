"""
- Use all to determine if all elements of an iterable are True.
- It's faster, uses less memory, and you'll see it everywhere anyway.
- Note that the two quotes represent the delimiter between list elements in the string we're creating.
"""

# Harmful solution
def contains_zero(iterable):
    for e in iterable:
        if e == 0:
            return True

    return False


# Idiomatic solution
def contains_zero(iterable):
    # 0 is "Falsy," so this works
    return not all(iterable)
