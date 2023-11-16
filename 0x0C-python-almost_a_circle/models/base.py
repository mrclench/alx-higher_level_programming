#!/usr/bin/python3
"""Creating a class named Base"""

import json

"""imports json"""


class Base:
    """This is the base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
                not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if not isinstance(list_objs, list) and list_objs is not None:
            raise TypeError("list_objs must be a list of instances")

            # Convert list of instances to list of dictionaries
        list_dicts = [x.to_dictionary() for x in list_objs] if list_objs is not None else []

        # Create the filename using the class name
        filename = cls.__name__ + ".json"

        # Write the JSON string representation to the file
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

            Args:
                **dictionary: Double pointer to a dictionary with attribute values.

            Returns:
                An instance of the class with attributes set based on the dictionary.
            """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""

        filename = cls.__name__ + ".json"
        new_loader = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dicts = cls.from_json_string(s)
                for d in list_dicts:
                    new_loader.append(cls.create(**d))
        return new_loader

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs in CSV format and saves it to a file."""

        if (type(list_objs) != list and
                list_objs is not None or
                not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """A method that serializes and deserializes a list of instances."""

        filename = cls.__name__ + ".csv"
        new_load = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        new_load.append(i)
        return new_load

    @staticmethod
    def draw(list_rectangles, list_squares):
        """A static method that opens a window and draws all the instances"""

        import turtle
        import time
        from random import randrange

        t = turtle.Turtle()
        t.color("beige")
        turtle.bgcolor("violet")
        t.shape("square")
        t.pensize(8)

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(t, i)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_rect(t, rect):
        """Helper method that draws a Rectangle
        or Square.
        """

        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
