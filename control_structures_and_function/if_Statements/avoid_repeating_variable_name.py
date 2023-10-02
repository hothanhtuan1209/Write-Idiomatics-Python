"""
- Avoid repeating variable name in compound if statement
- When you want to check a variable against a number of values, repeatedly listing the variable being checked is unnecessarily verbose.
- Using a check for existence in a list or set makes the code more clear and improves readability.
"""

# Harmful solution
# is_generic_name = False
# name = "Tom"

# if name == "Tom" or name == "Dick" or name == "Harry":
#     is_generic_name = True


# Idiomatic solution
name = "Tom"
is_generic_name = name in ("Tom", "Dick", "Harry")
