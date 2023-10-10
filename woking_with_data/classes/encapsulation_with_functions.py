"""
- Don't use classes solely as a form of encapsulation.
- Instead, use modules to encapsulate related functions.
- Modules are the preferred unit of encapsulation, and you can use 'all'
to control which functions are importable from a module.
"""

# Harmful solution
# class StringUtils():
#     def reverse(self, string):
#         return reversed(string)

#     def count_occurrences(self, string, key):
#         return sum([1 for c in string if c == key])

#     def is_palindrome(self, string):
#         for index in range(len(string)//2):

#             if string[index] != string[-index-1]:
#                 return False

#         return True

# s = StringUtils()


# Idiomatic solution
def reverse(string):
    """
    Reverses a given input string.

    Parameter:
        string (str): The string to be reversed.

    return:
        str: The reversed string.
    """

    return reversed(string)


def count_occurrences(string, key):
    """
    Counts the number of occurrences of a character or substring in the
    input string.

    Args:
        string (str): The string to count occurrences in.
        key (str): The character or substring to count.

    Returns:
        int: The number of times 'key' appears in 'string'.
    """

    return sum([1 for c in string if c == key])


def is_palindrome(string):
    """
    Checks if a string is a palindrome (reads the same forwards and backwards).

    Args:
        string (str): The string to check.

    Returns:
        bool: True if 'string' is a palindrome, False otherwise.
    """

    for index in range(len(string)//2):

        if string[index] != string[-index-1]:
            return False

    return True
