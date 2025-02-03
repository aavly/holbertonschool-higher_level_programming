#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""


class BaseGeometry():
    """
    Class to define BaseGeometry.

    Raises:
        Exception:	area() is not implemented
        TypeError: <name> must be an integer
        ValueError: <name> must be greater than 0
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Class to define Rectangle that inherits BaseGeometry.

    Private attributes:	width
                        height

    Raises:
        Exception:	area() is not implemented
        TypeError:	<name> must be an integer
                    height must be an integer
                    width must be an integer
        ValueError:	<name> must be greater than 0
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def integer_validator(self, width, height):
        if not isinstance(self.__width, int):
            raise TypeError("width must be an intger")
        if not isinstance(self.__height, int):
            raise TypeError("height must be an intger")
