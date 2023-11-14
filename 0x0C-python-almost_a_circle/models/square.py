#!/usr/bin/python3
"""This module defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle class

    Methods:
        __init__(self, size, x=0, y=0, id=None): Initializes a new Square instance.
        __str__(self): Returns a string representation of the square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the class Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Printing string value of height and weight"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """getting size"""
        return self._size

    @size.setter
    def size(self, value):
        """setting size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self._size = value