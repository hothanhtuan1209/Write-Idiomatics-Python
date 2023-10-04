"""
- Use the isinstance function to determine the type of an object.
- The isinstance function checks if an object matches a specified type or
types, returning True if there's a match.
- It's typically used for built-in types but can work with user-defined types
as well.
"""

# Harmful solution
# def get_size(some_object):
#     """
#     Return the "size" of *some_object*, where size = len(some_object) for
#     sequences, size = some_object for integers and floats, and size = 1 for
#     True, False, or None.
#     """

#     try:
#         return len(some_object)

#     except TypeError:
#         if some_object in (True, False, type(None)):
#             return 1

#         else:
#             return int(some_object)

# print(get_size('hello'))
# print(get_size([1, 2, 3, 4, 5]))
# print(get_size(10.0))


# Idiomatic solution
def get_size(some_object):
    """
    Return the "size" of *some_object*, where size = len(some_object) for
    sequences, size = some_object for integers and floats, and size = 1 for
    True, False, or None.
    """

    if isinstance(some_object, (list, dict, str, tuple)):
        return len(some_object)

    elif isinstance(some_object, (bool, type(None))):
        return 1

    elif isinstance(some_object, (int, float)):
        return int(some_object)


print(get_size('hello'))
print(get_size([1, 2, 3, 4, 5]))
print(get_size(10.0))
