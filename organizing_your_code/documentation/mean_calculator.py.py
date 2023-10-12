"""
- Use Inline Documentation Sparingly.
- Using inline documentation excessively can be counterproductive.
"""


# Harmful solution
# def calculate_mean(numbers):
#     """Return the mean of a list of numbers"""

#     # If the list is empty, we have no mean!
#     if not numbers:
#         return 0

#     # A variable to keep track of the running sum
#     total = 0

#     # Iterate over each number in the list
#     for number in numbers:
#         total += number

#     # Divide the sum of all the numbers by how
#     # many numbers were in the list
#     # to arrive at the sum. Return this value.
#     return total / len(numbers)


# Idiomatic solution
def calculate_mean(numbers):
    """Return the mean of a list of numbers"""

    return sum(numbers) / len(numbers)
