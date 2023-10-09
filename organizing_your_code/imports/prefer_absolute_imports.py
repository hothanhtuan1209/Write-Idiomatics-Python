"""
- Prefer absolute imports to relative imports.
- Prefer absolute imports over relative imports to avoid cluttering the
module's namespace and provide clarity on where the imported module is defined.
"""


# Harmful solution
# My location is package.sub_package.module
# and I want to import package.other_module.
# The following should be avoided:
# from ...package import other_module


# Idiomatic solution
# My location is package.sub_package.another_sub_package.module
# and I want to import package.other_module.
# Either of the following are acceptable:
import package.other_module
import package.other_module as other
