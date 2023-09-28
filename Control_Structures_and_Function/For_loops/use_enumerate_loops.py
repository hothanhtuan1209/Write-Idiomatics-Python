"""
- Use the enumerate function in loops instead of creating an “index” variable
- Other languages explicitly declaring a variable to track the index of a container in a loop but in python, the enumerate built-in function handles this role.
"""

# You shouldn't do like this
my_container = ["Larry", "Moe", "Curly"]
index = 0

for element in my_container:
    print("{} {}".format(index, element))
index += 1


# You should do like this
my_container = ["Larry", "Moe", "Curly"]
for index, element in enumerate(my_container):
    print("{} {}".format(index, element))
