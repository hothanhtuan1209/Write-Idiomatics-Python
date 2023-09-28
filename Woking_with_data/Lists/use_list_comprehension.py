"""
- Use a list comprehension to create a transformed version of an existing list.
- List comprehensions, when used wisely, improve code clarity when constructing lists from existing data, especially when elements are checked and transformed.
"""

# Harmful solution
some_other_list = range(10)
some_list = list()

for element in some_other_list:
    if is_prime(element):
        some_list.append(element + 5)


# Idiomatic solution
some_other_list = range(10)
some_list = [element + 5 for element in some_other_list if is_prime(element)]
