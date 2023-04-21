#!/usr/bin/python3
"""Inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """defines a class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new instance of a rectangle.
        Attributes:
        id (int): The id of the rectangle
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        x (int): a value affiliated with the rectangle. Default is 0.
        y (int): a value affiliated with the rectangle. Default is 0.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get/set the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Get/set the current x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Get/set the current y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
