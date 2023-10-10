"""
- Do not use from foo import * to import the contents of a module.
- Instead, group import statements within parentheses or use absolute imports
with an "as" clause to keep your namespace clean and organized.
"""


# Idiomatic solution
from foo import (bar, baz, qux,
        quux, quuux)
import foo


# Harmful solution
# from foo import *
