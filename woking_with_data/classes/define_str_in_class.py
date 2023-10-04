"""
- Define __str__ in a class to show a human-readable representation.
- When defining a class that is likely to be used with print(), the default
Python representation isn't too helpful.
- By defining a __str__ method, you can control how calling print on an
instance of your class will look.
"""

# Harmful solution
# class Point():
#     def __init__(self, first_value, second_value):
#         self.first_value = first_value
#         self.second_value = second_value

# point = Point(1, 2)
# print(point)
# Prints '<__main__.Point object at 0x91ebd0>'


# Idiomatic solution
class Point():
    """
    A class representing a point in a two-dimensional space.
    """

    def __init__(self, variable_1, variable_2):
        """
        Initialize a Point object with x and y coordinates.
        """

        self.variable_1 = variable_1
        self.variable_2 = variable_2

    def __str__(self):
        """
        Return a string representation of the Point object.
        """
        return '{0}, {1}'.format(self.variable_1, self.variable_2)


point = Point(1, 2)
print(point)
# Prints '1, 2'
