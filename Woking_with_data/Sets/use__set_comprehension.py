"""
- Use a set comprehension to generate sets concisely
- The set comprehension syntax is relatively new in Python and, therefore, often overlooked.
- Just as a list can be generated using a list comprehension, a set can be generated using a set comprehension.
"""

# Harmful solution
users_first_names = set()
for user in users:
    users_first_names.add(user.first_name)


# Idiomatic solution
users_first_names = {user.first_name for user in users}
