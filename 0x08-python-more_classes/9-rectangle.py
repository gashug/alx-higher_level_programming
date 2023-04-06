#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represents a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle

        Args:
            width(int): The width of the new square
            height(int): The height of the new square
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the current area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the distance round the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        The # character represents the rectangle.
        """
        if self.height == 0 or self.width == 0:
            return ""
        else:
            rec_shape = ""
            for i in range(self.height):
                rec_shape += "#" * self.width
                if i < self.height - 1:
                    rec_shape += "\n"
        return rec_shape

    def __repr__(self):
        """Return a string rep. of the rectangle"""
        return "Rectangle({0}, {1})".format(self.width, self.height)

    def __del__(self):
        """Deletes an instance of a rectangle"""
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area"""
        if not isinstance (rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance (rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle instance with height and width equated to size"""
        return cls(size, size)
