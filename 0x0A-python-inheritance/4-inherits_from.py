#!/usr/bin/python3
"""object instance checking function"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class 
        inherited from a specified class"""

    if type(obj) == a_class:
        return False
    elif issubclass(type(obj), a_class):
        return True
    else:
        return False
