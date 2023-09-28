"""
Avoid comparing directly to True, False, or None
"""

# You shouldn't do like this
def number_of_evil_robots_attacking():
    return 10

def should_raise_shields():
    return number_of_evil_robots_attacking()

if should_raise_shields() == True:
    raise_shields()
    print('Shields raised')
else:
    print('Safe! No giant robots attacking')

# You should do like this
def number_of_evil_robots_attacking():
    return 10

def should_raise_shields():
    return number_of_evil_robots_attacking()

if should_raise_shields():
    raise_shields()
    print('Shields raised')
else:
    print('Safe! No giant robots attacking')
