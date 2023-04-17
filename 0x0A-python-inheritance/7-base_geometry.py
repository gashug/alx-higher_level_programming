#!/usr/bin/python3
"""Define an empty class BaseGeometry"""


class BaseGeometry:
    """Represents a shape"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
