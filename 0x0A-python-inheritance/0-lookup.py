#!/usr/bin/python3
"""an attribute returning function"""


def lookup(obj):
    """Returns the list of available attributes."""
    return dir(obj)
