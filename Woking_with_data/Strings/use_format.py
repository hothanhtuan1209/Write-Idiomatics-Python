"""
- Prefer the format function for formatting strings.
- There are three general ways of formatting strings in Python: using the + operator to concatenate a mix of static strings and variables, using "old-style" string formatting with a format string and the % operator, and using the format function. 
- The clearest and most idiomatic way is to use the format function.
"""

# Harmful solution
def get_formatted_user_info_worst(user):
    return "Name: " + user.name + ", Age: " + str(user.age) + ", Sex: " + user.sex


def get_formatted_user_info_slightly_better(user):
    return "Name: %s, Age: %i, Sex: %c" % (user.name, user.age, user.sex)


# Harmful solution
def get_formatted_user_info(user):
    output = "Name: {user.name}, Age: {user.age}, Sex: {user.sex}".format(user=user)

    return output
