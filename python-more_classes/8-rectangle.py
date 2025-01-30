#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by:
(based on 7-rectangle.py)
"""


class Rectangle:
    """
    Class to define Rectangle.

    Private instance attribute: width
                                height

    Public class attribute: number_of_instances
                            print_symbol

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
        stri = ""
        newline = "\n"

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                stri += str(self.print_symbol)
            if i != self.__height - 1:
                stri += newline
        return stri

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

    # Static method
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1


my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")
