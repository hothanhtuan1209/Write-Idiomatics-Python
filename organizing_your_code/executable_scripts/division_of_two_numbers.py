"""
- Use the if __name__ == '__main__' pattern to allow a file to be both
imported and run directly.
- If you want a file to function both as an importable Python module and a
stand-alone script, use the if __name__ == '__main__' idiom.
"""


import sys
import os


# Harmful solution
# FIRST_NUMBER = float(sys.argv[1])
# SECOND_NUMBER = float(sys.argv[2])


# def divide(first_parameter, second_parameter):
#     return first_parameter / second_parameter

# I can't import this file (for the super
# useful 'divide' function) without the following
# code being executed.


# if SECOND_NUMBER != 0:
#     print(divide(FIRST_NUMBER, SECOND_NUMBER))


# Idiomatic solution
def divide(first_parameter, second_parameter):
    """
    Divide the first parameter by the second parameter.

    Parameters:
        first_parameter (float): The divisor.
        second_parameter (float): The divisor.

    Returns:
        int: The result of dividing the first parameter by the second
        parameter.

    """

    return first_parameter / second_parameter

# Will only run if script is executed directly,
# not when the file is imported as a module


if __name__ == '__main__':
    first_number = float(sys.argv[1])
    second_number = float(sys.argv[2])
    if second_number != 0:
        print(divide(first_number, second_number))
