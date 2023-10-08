"""
- Prefer a generator expression to a list comprehension for simple iteration.
- List comprehension: It creates a list and immediately fills all the elements
of that list. This can take up a lot of memory if you have a large list.
- Generator expression: It creates a generator, and instead of creating the
complete list from scratch, it just generates each element of the list "on
demand" as you iterate over it. This saves memory and allows you to work with
large lists or even infinite strings without resource issues.
"""

# Harmful solution
# def get_all_usernames():
#     pass


# def process_normalized_username():
#     pass


# for uppercase_name in [name.upper() for name in get_all_usernames()]:
#     process_normalized_username(uppercase_name)


# Idiomatic solution
def get_all_usernames():
    pass


def process_normalized_username():
    pass


for uppercase_name in (name.upper() for name in get_all_usernames()):
    process_normalized_username()
