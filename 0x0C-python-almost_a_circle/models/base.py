#!/usr/bin/python3
"""defines the class Base"""


class Base():
    """"empty class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base class with id

        Args:
            id (int)
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
