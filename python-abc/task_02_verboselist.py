#!/usr/bin/python3
"""Extending the Python List with Notifications"""


class VerboseList(list):
    """
    Class VerboseList that extends the Python 'list' class.
    VerboseList should print a notif msg everytime an item is 
    added or removed.
    """
    def __init__(self, list=[]):
        self.__list = list

    def append(self, item):
        super().append(item)
        print("Added {} to the list".format(item))

    def extend(self, list_to_add):
        super().extend(list_to_add)
        print("Extended the list with {} items".format(len(list_to_add)))

    def remove(self, item):
        if item in self.__list:
            print("Removed {} from the list".format(item))
            super().remove(item)

    def pop(self, item=None):
        if item in self.__list:
            print("Popped {} from the list".format(item))
            super().pop(item)

# Testing
vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)