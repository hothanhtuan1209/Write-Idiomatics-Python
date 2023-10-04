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
    def __init__(self, first_value, second_value):
        """
        Initialize a Point object with x and y coordinates.
        """

        self.first_value = first_value
        self.second_value = second_value

    def __str__(self):
        """
        Return a string representation of the Point object.
        """
        return '{0}, {1}'.format(self.first_value, self.second_value)


point = Point(1, 2)
print(point)
# Prints '1, 2'
