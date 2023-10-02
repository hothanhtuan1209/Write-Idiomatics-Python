"""
- Use _ as a placeholder for data in a tuple that should be ignored.
- When setting a tuple equal to some ordered data, oftentimes not all of the data is actually needed.
- Instead of creating throwaway variables with confusing names, use the _ as a placeholder to tell the reader, “This data will be discarded.”
"""

# Harmful solution
# (name, age, temp, temp2) = get_user_info(user)

# if age > 21:
#     output = '{name} can drink!'.format(name=name)
# "Wait, where are temp and temp2 being used?"


# Idiomatic solution
(name, age, _, _) = get_user_info(user)

if age > 21:
    output = '{name} can drink!'.format(name=name)
# "Clearly, only name and age are interesting"
