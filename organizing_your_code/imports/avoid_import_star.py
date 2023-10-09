"""
- Do not use from foo import * to import the contents of a module.
- Instead, group import statements within parentheses or use absolute imports
with an "as" clause to keep your namespace clean and organized.
"""


# Harmful solution
# from foo import *


# Idiomatic solution
from foo import (bar, baz, qux,
        quux, quuux)

# or even better...
import foo
