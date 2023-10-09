"""
- Use sys.exit in your script to return proper error codes.
- Use sys.exit within main to return error codes on issues or zero for
successful execution.
- The only code under if __name__ == '__main__' should call sys.exit(main())
"""


import sys


# Harmful solution
# if __name__ == '__main__':
#     import sys

     # What happens if no argument is passed on the
     # command line?
     # if len(sys.argv) > 1:
     #     argument = sys.argv[1]
     #     result = do_stuff(argument)

     # Again, what if this is False? How would other
     # programs know?

     # if result:
     #     do_stuff_with_result(result)


# Idiomatic solution
def do_stuff(argument):
    return True


def do_stuff_with_result(result):
    pass


def main():
    if len(sys.argv) < 2:
        # Calling sys.exit with a string automatically
        # prints the string to stderr and exits with
        # a value of '1' (error)

        sys.exit('You forgot to pass an argument')
    argument = sys.argv[1]
    result = do_stuff(argument)
    if not result:
        sys.exit(1)
        # We can also exit with just the return code

    do_stuff_with_result(result)

    # Optional, since the return value without this return
    # statment would default to None, which sys.exit treats
    # as 'exit with 0'
    return 0

# The two lines below are the canonical script entry
# point lines. You'll see them often in other Python scripts


if __name__ == '__main__':
    sys.exit(main())
