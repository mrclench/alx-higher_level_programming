#!/usr/bin/python3
"""Creating a new class called Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the class Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Printing string value of height and weight"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
