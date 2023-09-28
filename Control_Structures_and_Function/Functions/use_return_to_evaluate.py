"""
- Use return to evaluate expressions in addition to return values.
- The return statement in functions returns the result of an expression.
- Variables are evaluated to their values, so it's more concise to directly return the result of an expression, instead of assigning it to a variable and then returning the variable on the next line.
"""

# You shouldn't do like this
def all_equal(a, b, c):
    result = False
    if a == b == c:
        result = True
    return result


# You should do like this
def all_equal(a, b, c):
    return a == b == c
