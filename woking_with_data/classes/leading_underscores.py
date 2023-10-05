"""
- Use leading underscores in function and variable names to denote “private”
data.
- In Python, all attributes of a class, including data and methods, are
inherently "public" by default, which means they can be accessed from outside
the class.
- To ensure privacy and prevent naming conflicts, Python follows naming
conventions:
    1. To mark attributes as "protected" (not intended for direct external
    access), a single underscore prefix (_) is used.
    2. To mark attributes as "private" (not intended for direct access or
    subclass override), a double underscore prefix (__) is used.
"""
import pytest

# Harmful solution
# class Foo():
#     def __init__(self):
#         self.id = 8
#         self.value = self.get_value()

#     def get_value(self):
#         pass

#     def should_destroy_earth(self):
#         return self.id == 42


# class Baz(Foo):
#     def get_value(self, some_new_parameter):
#         """Since 'get_value' is called from the base class's
#         __init__ method and the base class definition doesn't
#         take a parameter, trying to create a Baz instance will
#         fail.
#         """

#         pass


# class Qux(Foo):
#     """We aren't aware of Foo's internals, and we innocently
#     create an instance attribute named 'id' and set it to 42.
#     This overwrites Foo's id attribute and we inadvertently
#     blow up the earth.
#     """

#     def __init__(self):
#         super(Qux, self).__init__()
#         self.id = 42

#     # No relation to Foo's id, purely coincidental

# qux = Qux()
# baz = Baz() # Raises 'TypeError'
# qux.should_destroy_earth() # returns True
# qux.id == 42 # returns True


# Idiomatic solution
class Foo():
    """
    A class representing a Foo object.
    """

    def __init__(self):
        """
        Since 'id' is of vital importance to us, we don't
        want a derived class accidentally overwriting it. We'll
        prepend with double underscores to introduce name
        mangling.
        """

        self.__id = 8
        self.value = self.__get_value()  # Our 'private copy'

    def get_value(self):
        """
        Get the value
        """

        pass

    def should_destroy_earth(self):
        """
        Check if '__id' is equal to 42.

        Returns:
            bool: True if '__id' is equal to 42, False otherwise.
        """

        return self.__id == 42

    def __get_value(self):
        """
        A 'private copy' of the 'get_value' method.
        """

        return self.get_value()


class Baz(Foo):
    def get_value(self, some_new_parameter=None):
        pass


class Qux(Foo):
    def __init__(self):
        """Now when we set 'id' to 42, it's not the same 'id'
        that 'should_destroy_earth' is concerned with. In fact,
        if you inspect a Qux object, you'll find it doesn't
        have an __id attribute. So we can't mistakenly change
        Foo's __id attribute even if we wanted to.
        """

        self.id = 42
        # No relation to Foo's id, purely coincidental
        super(Qux, self).__init__()


qux = Qux()
baz = Baz()  # Works fine now
print(qux.should_destroy_earth())  # returns False
print(qux.id == 42)  # returns True
with pytest.raises(AttributeError):
    getattr(qux, "__id")
