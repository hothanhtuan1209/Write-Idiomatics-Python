"""
- Avoid using a mutable object as the default value for a function argument.
- Default arguments in Python are computed only once when the function is defined. 
"""

# Harmful solution
# def f(a, L=[]):
#     L.append(a)

#     return L

# print(f(1))
# print(f(2))
# print(f(3))


# Idiomatic solution
def examp(value_append, list_examp=None):
    """
    Append a value to a list or create a new list if not provided.

    Args:
        value_append: The value to append.
        list_examp (list, optional): The list to append the value to. If not provided, a new list is created.

    Returns:
        list: The list with the appended value.
    """

    if list_examp is None:
        list_examp = []
        list_examp.append(value_append)

    return list_examp

print(examp(1))
print(examp(2))
print(examp(3))
