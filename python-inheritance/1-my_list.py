#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        print(sorted(self))
