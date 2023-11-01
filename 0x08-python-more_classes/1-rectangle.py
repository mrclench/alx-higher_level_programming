#!/usr/bin/python3
"""Defining a class named Rectangle"""


class Rectangle:
    """Defining a class named Rectangle"""
    def __init__(self, width=0, height=0):
        """initializing the class Rectangle
        Args: width=0: width of the Rectangle
        Args: height=0: height of the rectangle"""
        self.height = height
        self.width = width
    @property
    def width(self):
        """Getting width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getting the height of the square"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value