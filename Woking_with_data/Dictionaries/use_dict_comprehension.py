"""
- Use a dict comprehension to build a dict clearly and efficiently.
- The list comprehension is a well-known Python construct.
- Less well known is the dict comprehension.
"""

# Harmful solution
user_email = {}

for user in users_list:
    if user.email:
        user_email[user.name] = user.email


# Idiomatic solution
user_email = {user.name: user.email
                for user in users_list if user.email}
