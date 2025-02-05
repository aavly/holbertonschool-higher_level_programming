#!/usr/bin/python3
"""
CountedIterator - Keeping Track of Iteration
"""


class CountedIterator():
    """
    Class CounterIterator which keeps track of the number of items
    that have been iterated over.
    """

    counter = 0

    def __init__(self, obj):
        objct = iter(obj)
        CountedIterator.counter += 1

    def get_count(self):
        return CountedIterator.counter

    # Overriding __next__ method
    def __next__(self):
        CountedIterator.counter += 1
    