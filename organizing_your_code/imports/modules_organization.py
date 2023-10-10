"""
- Use the tuples to organize a long list of modules to import.
- To manage long lists of module imports more effectively, consider using
tuples to group multiple imports within a single import statement, making
the code cleaner and more organized.
"""


# Idiomatic solution
from django.db.models import (AutoField, BigIntegerField, BooleanField,
        CharField, CommaSeparatedIntegerField, DateField, DateTimeField)


# Harmful solution
# from django.db.models import AutoField, BigIntegerField, BooleanField, CharField
# from django.db.models import CommaSeparatedIntegerField, DateField, DateTimeField
