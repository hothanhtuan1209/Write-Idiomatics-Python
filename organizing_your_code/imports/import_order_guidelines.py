"""
- Arrange your import statements in a standard order.
- It's advisable to place all import statements at the top of each file,
choose a standard order for your import statements, and consistently follow it.
- While the specific ordering is not critical, Python's Programming FAQ
recommends the following order:
    1. Standard library modules.
    2. Third-party library modules installed in site-packages.
    3. Modules local to the current project.
"""


# Idiomatic solution
import concurrent.futures
import os.path
import sys
from flask import (Flask, request, session, g,
    redirect, url_for, abort,
    render_template, flash, _app_ctx_stack)
import requests
import this_project.utilities.sentient_network as skynet
import this_project.widgets


# Harmful solution
# import os.path
# # Some function and class definitions,
# # one of which uses os.path
# # ....

# import concurrent.futures
# from flask import render_template

# # Stuff using futures and Flask's render_template
# # ....

# from flask import (Flask, request, session, g,
#     redirect, url_for, abort,
#     render_template, flash, _app_ctx_stack)
# import requests

# # Code using flask and requests
# # ....

# if __name__ == '__main__':
#     # Imports when imported as a module are not so
#     # costly that they need to be relegated to inside
#     # an 'if __name__ == '__main__'' block...
#     import this_project.utilities.sentient_network as skynet
#     import this_project.widgets
#     import sys
