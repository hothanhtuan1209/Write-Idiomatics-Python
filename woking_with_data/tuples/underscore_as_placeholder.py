"""
- Use _ as a placeholder for data in a tuple that should be ignored.
- When setting a tuple equal to some ordered data, oftentimes not all
of the data is actually needed.
- Instead of creating throwaway variables with confusing names, use the _ as
a placeholder to tell the reader, “This data will be discarded.”
"""

# Harmful solution
# (name, age, temp, temp2) = get_user_info(user)

# if age > 21:
#     output = '{name} can drink!'.format(name=name)
# "Wait, where are temp and temp2 being used?"


# Idiomatic solution
def get_user_info(user):
    """
    Get user information including name and age.

    Args:
        user (dict): A dictionary containing user data.

    Returns:
        tuple: A tuple containing user name (str), age (int), and two
        placeholders.
    """

    return user.get("name", ""), user.get("age", 0), None, None


user_data = {"name": "John", "age": 25}

(name, age, _, _) = get_user_info(user_data)

if age > 21:
    output = "{name} can drink!".format(name=name)

else:
    output = "{name} cannot drink!".format(name=name)

print(output)
