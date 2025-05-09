#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """
    Class to define a Square based on 3-square.py

    Private instance attribute: size
        property def size(self) to retrieve it - getter
        property setter def size (self, value): to set it:

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    # Instantiation with optional size
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """ Public instance method that returns the current square area"""
        sq_area = pow(self.__size, 2)
        return sq_area

    # Getter
    @property
    def size(self):
        return self.__size

    # Setter
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
