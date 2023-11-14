#!/usr/bin/python3
"""Creating a class named Base"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @property
    def id(self):
        """Getting id of the base"""
        return self.__id

    @id.setter
    def id(self, value):
        """Setting ID of the rectangle"""
        self.__id = value
