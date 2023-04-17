#!/usr/bin/python3
"""a class that inherits from list"""


class MyList(list):
    """
    Custom list class that inherits from list.
    """

    
    def print_sorted(self):
        """Prints list in sorted order"""
        sorted_list = list.sort(self)
        return sorted_list
