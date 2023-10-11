"""
- Prefer absolute imports to relative imports.
- Prefer absolute imports over relative imports to avoid cluttering the
module's namespace and provide clarity on where the imported module is defined.
- Use the tuples to organize a long list of modules to import.
- To manage long lists of module imports more effectively, consider using
tuples to group multiple imports within a single import statement, making
the code cleaner and more organized.
- Do not use from foo import * to import the contents of a module.
- Instead, group import statements within parentheses or use absolute imports
with an "as" clause to keep your namespace clean and organized.
"""


# Rules about the order of import commands
import os.path
import sys
import requests

from flask import (Flask, request, session, g,
    redirect, url_for, abort,
    render_template, flash, _app_ctx_stack)
from django.db.models import (AutoField, BigIntegerField, BooleanField,
    CharField, CommaSeparatedIntegerField, DateField, DateTimeField)

import package.other_module
import package.other_module as other
from foo import (bar, baz, qux,
    quux, quuux)
import concurrent.futures
import this_project.utilities.sentient_network as skynet
import this_project.widgets


# Use a try block to determine if a package is available.
try:
    import cProfile as profiler

except:
    import profile as profiler
print(profiler.__all__)


# Idiomatic solution
my_list = []
for element in my_list:
    print(element)
    print('--------')

    # Avoid placing multiple statements on a single line
    # for element in my_list: print(element); print('--------')
