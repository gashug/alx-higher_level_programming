#!/usr/bin/python3
class Square:
    """Square is a four-sided mathematical figure
    whose sides are equal in length"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
