#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by:
(based on 6-rectangle.py)
"""


class Rectangle:
    """
    Class to define Rectangle.

    Private instance attribute: width
                                height

    Public class attribute: number_of_instances

    Raises:
        TypeError:	width must be an integer
                    height must be an integer

        ValueError: width must be >= 0
                    height must be >= 0
    """

    # Public Class attributes
    number_of_instances = 0
    print_symbol = "#"

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

        # Accessing class attribute using Class name
        Rectangle.number_of_instances += 1

    def __str__(self):
        str = ""
        newline = "\n"

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                str += self.print_symbol
            if i != self.__height - 1:
                str += newline
        return str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
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


my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
my_rectangle_1.print_symbol = "H"
print(my_rectangle_1)
my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)