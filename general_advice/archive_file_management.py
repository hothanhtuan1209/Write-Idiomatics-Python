"""
- Use functions in the os.path module when working with directory paths.
- Python has an entire module dedicated to functions on path names: os.path.
- Using os.path reduces the risk of common errors, makes your code portable,
and makes your code much easier to understand.
"""

import os
from datetime import date


# Harmful solution
# filename_to_archive = 'test.txt'
# new_filename = 'test.bak'
# target_directory = './archives'
# today = date.today()
# os.mkdir('./archives/' + str(today))
# os.rename(
#     filename_to_archive,
#     target_directory + '/' + str(today) + '/' + new_filename)


# Idiomatic solution

# Assign the current directory value to variable
current_directory = os.getcwd()
filename_to_archive = 'test.txt'

# Create a new filename in filename.bak format
new_filename = os.path.splitext(filename_to_archive)[0] + '.bak'

# Create target_directory by connect current_directory to archive folder
target_directory = os.path.join(current_directory, 'archives')
today = date.today()

# Create the new_path variable by concatenating target_directory with the
# current date converted to string.
new_path = os.path.join(target_directory, str(today))


if (os.path.isdir(target_directory)):
    # Check if the target_directory directory exists or not.

    if not os.path.exists(new_path):
        # Check if the new_path directory exists or not.

        # Create a new directory called new_path if it doesn't already exist.
        os.mkdir(new_path)

    os.rename(
        os.path.join(current_directory, filename_to_archive),
        os.path.join(new_path, new_filename))
