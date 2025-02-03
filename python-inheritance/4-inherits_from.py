#!/usr/bin/python3
"""
Write a function that returns True if the object is
an instance of a class that inherited (directly or indirectly)
the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    Function that checks if obj is an instance of a class
    that is inherited a_class (directly or indirectly).
    """
    if isinstance(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
