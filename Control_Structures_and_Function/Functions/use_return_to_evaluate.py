"""
- Use return to evaluate expressions in addition to return values.
- The return statement in functions returns the result of an expression.
- Variables are evaluated to their values, so it's more concise to directly return the result of an expression, instead of assigning it to a variable and then returning the variable on the next line.
"""

# Harmful solution
# def all_equal(a, b, c):
#     result = False
#     if a == b == c:
#         result = True
#     return result


# Idiomatic solution
def all_equal(a, b, c):
    """
    Check if three values are all equal.

    Args:
        a: The first value.
        b: The second value.
        c: The third value.

    Returns:
        bool: True
    """
    
    return a == b == c
