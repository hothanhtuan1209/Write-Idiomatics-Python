"""
- Use a context manager to ensure resources are properly managed.
"""

# Harmful solution
# file_handle = open(path_to_file, 'r')

# for line in file_handle.readlines():
#     if raise_exception(line):
#         print('No! An Exception!')


# Idiomatic solution
with open(path_to_file, 'r') as file_handle:
    
    for line in file_handle:
        if raise_exception(line):
            print('No! An Exception!')
