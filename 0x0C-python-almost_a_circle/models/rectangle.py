#!/usr/bin/python3
"""Creating a class rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the class rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getting width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the value of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getting height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getting X of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting x of the rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getting y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting y of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print stdout value in #"""
        for i in range(self.y):
            print()
            """This prints a new line"""
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Printing string values of id, weight, height, x, y"""
        return ("[Rectangle] ({}) {}/{} - {}"
                "/{}".format(self.id, self.x, self.y, self.width, self.height))


def update(self, *args):
    """Assigns an argument to each attribute"""
    if args:
        self.id = args[0]
    if len(args) > 1:
        self.width = args[1]
    if len(args) > 2:
        self.height = args[2]
    if len(args) > 3:
        self.x = args[3]
    if len(args) > 4:
        self.y = args[4]
