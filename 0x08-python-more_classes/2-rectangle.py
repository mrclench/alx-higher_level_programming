#!/usr/bin/python3
"""Creating a Rectangle class.

This class represents a rectangle with a width and height.
"""


class Rectangle:
    """Def of a rectangle class."""

    def __init__(self, width: int = 0, height: int = 0):
        """Initialize a new Rectangle object.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """Get or set the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value: int):
        """Set the width of the rectangle.

        Args:
            value: The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than zero.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """Get or set the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value: int):
        """Set the height of the rectangle.

        Args:
            value: The new height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than zero.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        """Calculate the area of the rectangle.

        Returns:
            The area of the rectangle.
        """

        return self.width * self.height

    def perimeter(self) -> int:
        """Calculate the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """

        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
