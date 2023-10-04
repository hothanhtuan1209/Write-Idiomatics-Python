"""
- Use properties to “future-proof” your class implementation.
- Use properties in classes to prepare for potential changes in attribute
handling.
- This allows you to add logic or calculations later without altering existing
code.
"""


# Harmful solution
# class Product():
#     def __init__(self, name, price):
#         self.name = name  # We could try to apply the tax rate here,
#         self.price = price  # may be modified later, which erases the tax


# Idiomatic solution
class Product():
    TAX_RATE = 0.10

    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        # now if we need to change how price is calculated, we can do it
        # here (or in the "setter" and __init__)
        return (self._price * self.TAX_RATE) + self._price

    @price.setter
    def price(self, value):
        # The "setter" function must have the same name as the property
        self._price = value


product = Product("lemon", 100.0)
print(product.price)
