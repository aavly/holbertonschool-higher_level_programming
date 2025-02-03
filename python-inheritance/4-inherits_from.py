#!/usr/bin/python3
"""
Write a function that returns True if the object is
an instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    Function that checks if obj is an instance of a_class
    that is inherited from the specifi
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False

