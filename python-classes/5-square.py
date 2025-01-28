#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """
    Class to define a Square based on 4-square.py

    Private instance attribute: size
        property def size(self) to retrieve it - getter
        property def size (self, value) - setter

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    # Instantiation with optional size
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def area(self):
        """ Public instance method that returns the current square area"""
        sq_area = pow(self.__size, 2)
        return sq_area

    def my_print(self):
        """ Prints in stdout the square with the char # """
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print('#', end="")
            print()

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
