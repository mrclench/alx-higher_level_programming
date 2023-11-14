#!/usr/bin/python3
"""Creating a class named Base"""


class Base:
    """Defining the class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing Base class"""

        self.id = id
        if self.id is not None:
            @property
            def id(self):
                return self.id

            @id.setter
            def id(self, value):

                self.id = value
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
