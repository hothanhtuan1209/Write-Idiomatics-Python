"""
- Use the built-in function sum to calculate the sum of a list of values
"""

# Harmful solution
the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
the_sum = 0

for element in the_list:
    the_sum += element


# Idiomatic solution
the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
the_sum = sum(the_list)
