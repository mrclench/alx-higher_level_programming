#!/usr/bin/python3
"""This module defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle class
    Square class that inherits from Rectangle class.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
        id (int): The identifier of the square.

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
