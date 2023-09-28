"""
- Learn to treat functions as values.
- In Python, functions are objects that can be assigned to variables, passed as arguments, and returned as results.
"""

# You shouldn't do like this
def print_addition_table():
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(x + y) + '\n')

def print_subtraction_table():
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(x - y) + '\n')

def print_multiplication_table():
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(x * y) + '\n')

def print_division_table():
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(x / y) + '\n')

print_addition_table()
print_subtraction_table()
print_multiplication_table()
print_division_table()

# You should do like this
import operator as op

def print_table(operator):
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(operator(x, y)) + '\n')

for operator in (op.add, op.sub, op.mul, op.itruediv):
    print_table(operator)
