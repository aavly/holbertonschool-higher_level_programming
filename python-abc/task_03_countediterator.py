#!/usr/bin/python3
"""
CountedIterator - Keeping Track of Iteration
"""


class CountedIterator():
    """
    Class CounterIterator which keeps track of the number of items
    that have been iterated over.
    """

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item

        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.counter
