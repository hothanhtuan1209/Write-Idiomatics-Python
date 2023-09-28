"""
- Learn to use keyword arguments properly.
- Keyword arguments in Python functions are parameters with default values that make them optional in function calls.
- They provide flexibility by allowing you to customize the function's behavior when needed, while still using predefined defaults when you don't specify them.
"""

# You shouldn't do like this
def print_list(list_value, sep):
    print('{}'.format(sep).join(list_value))

the_list = ['a', 'b', 'c']
the_other_list = ['Jeff', 'hates', 'Java']
print_list(the_list, ' ')
print_list(the_other_list, ' ')
print_list(the_other_list, ', ')

# You should do like this
def print_list(list_value, sep=' '):
    print('{}'.format(sep).join(list_value))

the_list = ['a', 'b', 'c']
the_other_list = ['Jeff', 'hates', 'Java']
print_list(the_list)
print_list(the_other_list)
print_list(the_other_list, ', ')
