#!/usr/bin/python3

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    @property
    def width(self):
      return self.__width
    @width.setter
    def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")

            if  value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
    @property
    def height(self):
      return self.__height
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
                raise ValueError("height must be > 0")
        self.__height = value
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        for _ in range(self.height):
            print("#" * self.width)
        """Used a throwaway variable to loop """

    def __str__(self):
        """Printing string values of id, weight, height, x, y"""
        return ("[Rectangle] ({}) {}/{} - {}"
                "/{}".format(self.id, self.x, self.y, self.width, self.height))

