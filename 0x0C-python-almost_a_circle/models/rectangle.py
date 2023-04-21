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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get/set the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/set the current x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set the current y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints in std out rectangle instance with #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns string rep of rectangle object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """Updates the attributes of the Rectangle"""

    if len(args) > 0:
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            elif i == 1:
                self.width = arg
            elif i == 2:
                self.height = arg
            elif i == 3:
                self.x = arg
            elif i == 4:
                self.y = arg
