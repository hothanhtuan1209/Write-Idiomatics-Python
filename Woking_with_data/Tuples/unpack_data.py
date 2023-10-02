"""
- Use tuples to unpack data.
- In Python, it is possible to “unpack” data for multiple assignment.
- Those familiar with LISP may know this as destructuring bind.
"""

# Harmful solution
# list_from_comma_separated_value_file = ['dog', 'Fido', 10]
# animal = list_from_comma_separated_value_file[0]
# name = list_from_comma_separated_value_file[1]
# age = list_from_comma_separated_value_file[2]
# output = ('{name} the {animal} is {age} years old'.format(
#     animal=animal, name=name, age=age))


# Idiomatic solution
list_from_comma_separated_value_file = ['dog', 'Fido', 10]
(animal, name, age) = list_from_comma_separated_value_file
output = ('{name} the {animal} is {age} years old'.format(
    animal=animal, name=name, age=age))
