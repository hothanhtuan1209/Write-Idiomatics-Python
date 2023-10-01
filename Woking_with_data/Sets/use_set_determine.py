"""
- Use sets to determine if two lists share any common values.
- Checking if any elements from one list appear in another.
- It simplifies the code by converting both lists to sets and finding common elements using the & operator, making the task easier and more efficient than using loops or other methods.
"""

# Harmful solution
# list_one = ['Manny', 'Moe', 'Jack']
# list_two = ['Larry', 'Moe', 'Curly']

# def has_duplicate(list_one, list_two):
#     duplicate_name = False
    
#     for name in list_one:
#         if name in list_two:
#             duplicate_name = True

#     return duplicate_name


# Idiomatic solution
list_one = ['Manny', 'Moe', 'Jack']
list_two = ['Larry', 'Moe', 'Curly']

def has_duplicate(list_one, list_two):
    """
    Check for duplicate elements between two lists.

    Parameters:
        list_one (list): The first list to check for duplicates.
        list_two (list): The second list to check for duplicates.

    Returns:
        set: A set containing elements that are duplicates between the two lists.
    """

    return set(list_one) & set(list_two)
