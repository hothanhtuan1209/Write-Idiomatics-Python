"""
- Avoid using a mutable object as the default value for a function argument.
- Default arguments in Python are computed only once when the function is defined. 
"""

# You shouldn't do like this
def f(a, L=[]):
    L.append(a)

    return L


print(f(1))
print(f(2))
print(f(3))


# You should do like this
def f(a, L=None):
    if L is None:
        L = []
        L.append(a)

    return L


print(f(1))
print(f(2))
print(f(3))
