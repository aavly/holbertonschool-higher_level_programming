#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by:
(based on 4-rectangle.py)
"""


class Rectangle:
    """
    Class to define Rectangle.

    Private instance attribute: width
                                height

    Raises:
        TypeError:	width must be an integer
                    height must be an integer

        ValueError: width must be >= 0
                    height must be >= 0
    """

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    def __str__(self):
        str = ""
        hash = "#"
        newline = "\n"

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                str += hash
            if i != self.__height - 1:
                str += newline
        return str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

    # Getters
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    # Setters
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Public instance methods
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
