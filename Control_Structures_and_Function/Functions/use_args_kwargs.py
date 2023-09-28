"""
- Use *args and **kwargs to accept arbitrary arguments.
- Can use *args to accept an arbitrary list of positional parameters and **kwargs for keyword parameters, which is helpful for flexibility and maintaining backward compatibility in functions.
"""

# You shouldn't do like this
def wrap_add_for_console_output(x, y):
    print('--------------------------------')
    print(str(x + y))
    print('--------------------------------')

wrap_add_for_console_output(2,3)

# You should do like this
def for_console_output(func):
    def wrapper(*args, **kwargs):
        print('--------------------------------')
        print(str(func(*args, **kwargs)))
        print('--------------------------------')
    
    return wrapper

@for_console_output
def add(x, y):
    return x + y
add(3, 2)
