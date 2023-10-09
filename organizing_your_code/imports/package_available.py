"""
- Use a try block to determine if a package is available.
- When writing libraries, one often needs to determine if a certain package
is available on a user's machine. If it is, it is imported and used. If not,
a fallback package must be used.
- The idiomatic way to perform this check is through the use of a try/ except
block.
"""


# Harmful solution
# import cProfile
# Uh-oh! The user doesn't have cProfile installed! Raise an exception
# here...
# print(cProfile.__all__)


# Idiomatic solution
try:
    import cProfile as profiler

except:
    import profile as profiler
print(profiler.__all__)
