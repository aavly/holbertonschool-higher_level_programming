#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """
    Class to define a Square based on 5-square.py

    Private instance attribute: size
        property def size(self) to retrieve it - getter
        property def size (self, value) - setter

    Private instance attribute: position
        property def position(self) to retrieve it - getter
        property def position (self, value) - setter

    Raises:
        TypeError:	size must be an integer
                    position must be a tuple of 2 positive integers
        ValueError: size must be >= 0
    """

    # Instantiation with optional size
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        """ Public instance method that returns the current square area"""
        return pow(self.__size, 2)

    def my_print(self):
        """ Prints in stdout the square with the char # """
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    # GETTERS
    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    # SETTERS
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        for i in range(2):
            if not isinstance(value[i], int) or value[i] < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = value
