#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """
    Class to define a Square based on 1-square.py

    Private instance attribute: size

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
