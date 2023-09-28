"""
- Use the in keyword to iterate over an iterable.
- Instead of using a loop you can use the in keyword instead
"""

# Harmful solution
my_list = ["Larry", "Moe", "Curly"]
index = 0

while index < len(my_list):
    print(my_list[index])
index += 1


# Idiomatic solution
my_list = ["Larry", "Moe", "Curly"]

for element in my_list:
    print(element)
