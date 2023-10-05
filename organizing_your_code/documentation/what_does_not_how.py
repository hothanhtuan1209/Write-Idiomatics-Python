"""
- Document what something does, not how.
- When writing docstring, focus on explaining what the code does rather than
how it achieves its functionality.
"""


# Harmful solution
# def is_prime(number):
#     """Mod all numbers from 2 -> number and return True
#     if the value is never 0"""

#     for candidate in range(2, number):
#         if number % candidate == 0:
#             print(candidate)
#             print(number % candidate)
#             return False

#     return number > 0


# Idiomatic solution
def is_prime(number):
    """Return True if number is prime"""

    for candidate in range(2, number):
        if number % candidate == 0:
            return False

    return number > 0
