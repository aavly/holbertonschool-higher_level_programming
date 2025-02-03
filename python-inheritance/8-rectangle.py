#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class to define Rectangle that inherits BaseGeometry.

    Private attributes:	width (int)
                        height (int)

    Raises:
        Exception:	area() is not implemented
        TypeError:	<name> must be an integer
                    height must be an integer
                    width must be an integer
        ValueError:	<name> must be greater than 0
    """
    def __init__(self, width, height):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
