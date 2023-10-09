"""
- Avoid placing multiple statements on a single line
- Though the language definition allows one to use ; to delineate statements,
doing so without reason makes one's code harder to read.
- When multiple statements occur on the same line as an if, else, or elif,
the situation is even further confused.
"""


# Harmful solution
# my_list = []
# for element in my_list: print(element); print('--------')


# Idiomatic solution
my_list = []
for element in my_list:
    print(element)
    print('--------')
