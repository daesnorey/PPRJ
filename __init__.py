"""
__init__.py adding folders to the __path__ object
"""

from sys import path

path.insert(0, "src/controllers")
