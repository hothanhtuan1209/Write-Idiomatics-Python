"""
Avoid comparing directly to True, False, or None
"""

# Harmful solution
# def number_of_evil_robots_attacking():
#     return 10


# def should_raise_shields():
#     return number_of_evil_robots_attacking()


# if should_raise_shields() == True:
#     raise_shields()
#     print("Shields raised")
# else:
#     print("Safe! No giant robots attacking")


# Idiomatic solution
def number_of_evil_robots_attacking():
    """
    Get the number of evil robots attacking.

    Returns:
        int: The number of evil robots currently attacking.
    """
    
    return 10


def should_raise_shields():
    """
    Check if shields should be raised against evil robots.

    Returns:
        int: The number of evil robots attacking.
    """
    
    return number_of_evil_robots_attacking()


if should_raise_shields():
    raise_shields()
    print("Shields raised")
else:
    print("Safe! No giant robots attacking")
