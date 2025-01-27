#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """
    Class to define a Square based on 2-square.py

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


    def area(self):
        """ Public instance method that returns the current square area"""
        if hasattr(self, 'size'):
            sq_area = pow(self.size, 2)
            print("Area: {}".format(sq_area))
        else:
            # not quite sure how to print attribute name
            print("'{}' object has no attribute '{}'".format(self, self.size))
        