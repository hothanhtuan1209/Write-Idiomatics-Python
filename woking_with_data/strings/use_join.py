"""
- Use ''.join when creating a single string for list elements.
- It's faster, uses less memory, and you'll see it everywhere anyway.
- Note that the two quotes represent the delimiter between list elements in the string we're creating.
"""

# Harmful solution
# result_list = ["True", "False", "File not found"]
# result_string = ""

# for result in result_list:
#     result_string += result


# Idiomatic solution
result_list = ["True", "False", "File not found"]
result_string = "".join(result_list)
