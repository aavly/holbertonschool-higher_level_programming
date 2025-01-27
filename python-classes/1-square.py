#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """
    Class to define a Square based on 0-square.py

    Private instance attribute: size

    Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        self.__size = size
