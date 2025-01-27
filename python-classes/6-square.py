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

    # Instantiation with optional size and optional position
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.size = size
        self.position = position

    def area(self):
        """Public instance method that returns the current square area"""
        if hasattr(self, 'size'):
            sq_area = pow(self.size, 2)
            print("Area: {}".format(sq_area))
        else:
            # not quite sure how to print attribute name
            print("'{}' object has no attribute '{}'".format(self, self.size))

    def my_print(self):
        """ Prints in stdout the square with the char # """
        if self.size == 0:
            print()
        elif isinstance(self.size, int) and self.size > 0:
            for i in range(self.size):
                for j in range(self.size):
                    print('#')

    # Getter
    @property
    def size(self):
        print("Retrieving Square Size...")
        return self.__size

    # Setter
    @size.setter
    def size(self, value):

        if value.isdigit():
            self.__size = value
        else:
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")

     # Getter
    @property
    def position(self):
        print("Retrieving Position Coordinates...")
        return self.__position

    # Setter
    @position.setter
    def position(self, value):

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value.isdigit():
            self.__position = value
