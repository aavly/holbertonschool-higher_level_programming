#!/usr/bin/python3
"""
Write a function that returns True if the object
is an instance of, or if the object is an instance
of a class that inherited from, the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Function that checks if obj is an
    instance of of a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
