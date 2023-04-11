#!/usr/bin/python3
"""Define a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height
        
        Args:
            width (int): Width of the Rectangle.
            height (int): Height of the Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle"""
        return self.width * self.height

    def __str__(self):
        """Returns given rectangle description"""
        string = '[' + str(self.__class__.__name__) + ']'
        string += str(self.__width) + '/' + str(self.__height)
        return string
