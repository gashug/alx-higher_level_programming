#!/usr/bin/python3
"""a class that inherits from list"""


class MyList(list):
    """
    Custom list class that inherits from list.
    """
    def __init__(self):
        """Initialize the object"""
        super().__init__()

    def print_sorted(self):
        """Prints list in sorted order"""
        print(sorted(self))
