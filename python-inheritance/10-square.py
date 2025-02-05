#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class to define Square that inherits Rectangle.

    Private attributes:	size (int)

    Raises:
        Exception:	area() is not implemented
            TypeError:	<name> must be an integer
            ValueError:	<name> must be greater than 0
    """
    def __init__(self, size):
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        return self.__size**2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
