#!/usr/bin/python3
"""object instance checking function"""


def is_kind_of_class(obj, a_class):
    """returns True if object is instance of specified class
        otherwise False
    """
    return isinstance(obj, a_class)
