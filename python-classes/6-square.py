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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in range(2):
            if position[i] < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """ Public instance method that returns the current square area"""
        sq_area = pow(self.__size, 2)
        return sq_area

    def my_print(self):
        """ Prints in stdout the square with the char # """
        if self.__size == 0:
            print()
        # printing spaces for y axis
        for y in range(self.__position[1]):
            print()
        for i in range(self.__size):
            # printing spaces for x axis
            for x in range(self.__position[0]):
                print(" ", end="")
                for j in range(self.__size):
                    print('#', end="")
                print()

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
        self.__size = value

    @position.setter
    def position(self, value):
        self.__position = value
