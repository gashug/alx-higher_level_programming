#!/usr/bin/python3
"""Square module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method for Rectangle class."""
        super().__init__(size,size, x, y, id)

    def __str__(self):
        """String rep. of Square object"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

        else:
            if kwargs and (not args or len(args) == 0):
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """"returns a dictionary rep of square"""
        return {'id' : self.id, 'size' : self.size, 
                'x' : self.x, 'y' :  self.y}
