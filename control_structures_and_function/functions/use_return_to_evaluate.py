"""
- Use return to evaluate expressions in addition to return values.
- The return statement in functions returns the result of an expression.
- Variables are evaluated to their values, so it's more concise to directly return the result of an expression, instead of assigning it to a variable and then returning the variable on the next line.
"""

# Harmful solution
# def all_equal(first_parameter, second_parameter, third_parameter):
#     result = False
#     if first_parameter == second_parameter == third_parameter:
#         result = True
#     return result


# Idiomatic solution
def all_equal(first_parameter, second_parameter, third_parameter):
    """
    Check if three values are all equal.

    Parameters:
        first_parameter: The first value.
        second_parameter: The second value.
        third_parameter: The third value.

    Returns:
        bool: True
    """
    
    return first_parameter == second_parameter == third_parameter
