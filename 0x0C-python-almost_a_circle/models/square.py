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
        self._size = size

    def __str__(self):
        """Printing string value of height and weight"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getting width of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setting width of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes"""
        attributes = ['id', 'size', 'x', 'y']

        if args:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        if kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returning the dictionary"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}