"""
- Use sys.argv to reference command line parameters.
- Instead of using complex libraries, Python allows command line parameter
checking using sys.argv for simple scripts. The name of the script will always
be the first parameter in the sys.argv list.
"""

import argparse


# Harmful solution
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(usage="my_cat.py <filename>")
#     parser.add_argument('filename', help='The name of the file to use')
#     parsed = parser.parse_args(sys.argv)
#     print(open(parsed['filename']).read())


# Idiomatic solution
if __name__ == '__main__':
    try:
        print(open(sys.argv[1]).read())

    except IndexError:
        print('You forgot the file name!')
