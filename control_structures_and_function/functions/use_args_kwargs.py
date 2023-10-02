"""
- Use *args and **kwargs to accept arbitrary arguments.
- Can use *args to accept an arbitrary list of positional parameters and **kwargs for keyword parameters, which is helpful for flexibility and maintaining backward compatibility in functions.
"""

# Harmful solution
# def wrap_add_for_console_output(x, y):
#     print("--------------------------------")
#     print(str(x + y))
#     print("--------------------------------")


# wrap_add_for_console_output(2, 3)


# Harmful solution
def for_console_output(func):
    """A decorator that prints a function's result with separators"""
    
    def wrapper(*args, **kwargs):
        print("--------------------------------")
        print(str(func(*args, **kwargs)))
        print("--------------------------------")

    return wrapper

@for_console_output
def add(first_number, second_number):
    """
    Add two numbers and return the result.

    Args:
        first_number (int): The first number.
        second_number (int): The second number.

    Returns:
        int: The sum of first_number and second_number.
    """

    return first_number + second_number

add(3, 2)
