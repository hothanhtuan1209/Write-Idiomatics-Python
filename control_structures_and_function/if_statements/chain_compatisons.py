"""
- When using if statements, make sure you're making the most out of the fact that comparisons can be chained arbitrarily.
- It both makes the statements more concise and can have a positive effect on performance.
"""

# Harmful solution
# def my_function():
#     x = 5
#     y = 10
#     z = 15

#     if x <= y and y <= z:
#         return True


# Idiomatic solution
def my_function():
    """Check if x is less than or equal to y and y is less than or equal to z."""

    x = 5
    y = 10
    z = 15

    if x <= y <= z:
        return True
