"""
- Use init.py files in Python packages to simplify package interfaces by
organizing and making module names available in a more user-friendly way
for external code.
"""


# Harmful solution
# If the gizmo directory has an emtpy __init__.py,
# imports like the ones below are necessary, even
# if Gizmo and GizmoHelper are all that clients should ever need to use
# from gizmo.client.interface import Gizmo
# from gizmo.client.contrib.utils import GizmoHelper


# Idiomatic solution
# __init__.py:

from gizmo.client.interface import Gizmo
from gizmo.client.contrib.utils import GizmoHelper

#client code:
from gizmo import Gizmo, GizmoHelper
