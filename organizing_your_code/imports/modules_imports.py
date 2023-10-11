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


# Idiomatic solutio
import package.other_module
import package.other_module as other
from django.db.models import (AutoField, BigIntegerField, BooleanField,
        CharField, CommaSeparatedIntegerField, DateField, DateTimeField)

from foo import (bar, baz, qux,
        quux, quuux)
import foo


# Harmful solution
# My location is package.sub_package.module
# and I want to import package.other_module.
# The following should be avoided:
# from ...package import other_module
# from django.db.models import AutoField, BigIntegerField, BooleanField, CharField
# from django.db.models import CommaSeparatedIntegerField, DateField, DateTimeField

# from foo import *
