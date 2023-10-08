"""
- Use __repr__ for a machine-readable representation of a class.
- In Python, __str__ is for human-readable representation, while __repr__ is
for machine-readable representation.
- A good __repr__ should contain all information to reconstruct an object, and
it should allow distinguishing between different instances.
"""

# Harmful solution
# class Foo():
#     def __init__(self, bar=10, baz=12, cache=None):
#         self.bar = bar
#         self.baz = baz
#         self._cache = cache or {}

#     def __str__(self):
#         return 'Bar is {}, Baz is {}'.format(self.bar, self.baz)

# def log_to_console(instance):
#     print(instance)

# log_to_console([Foo(), Foo(cache={'x': 'y'})])


# Idiomatic solution
class Foo():
    """
    A class representing a Foo object.
    """

    def __init__(self, bar=10, baz=12, cache=None):
        """
        Initialize a Foo object.

        Parameters:
            bar: An integer value for the 'bar' attribute (default is 10).
            baz: An integer value for the 'baz' attribute (default is 12).
            cache: A dictionary for caching data (default is an empty
            dictionary).
        """

        self.bar = bar
        self.baz = baz
        self._cache = cache or {}

    def __str__(self):
        """
        Return a string representation of the Foo object
        """

        return '{}, {}'.format(self.bar, self.baz)

    def __repr__(self):
        """
        Return a string representation of the Foo object for debugging and
        logging.
        """

        return 'Foo({}, {}, {})'.format(self.bar, self.baz, self._cache)


def log_to_console(instance):
    """
    Log an instance of Foo to the console.
    """

    print(instance)


log_to_console([Foo(), Foo(cache={'x': 'y'})])
