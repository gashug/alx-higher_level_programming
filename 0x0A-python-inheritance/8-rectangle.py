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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
