#!/usr/bin/python3
"""Extending the Python List with Notifications"""


class VerboseList(list):
    """
    Class VerboseList that extends the Python 'list' class.
    VerboseList should print a notif msg everytime an item is
    added or removed.
    """

    def append(self, item):
        print("Added [{}] to the list".format(item))
        super().append(item)

    def extend(self, list_to_add):
        print("Extended the list with [{}] items".format(len(list_to_add)))
        super().extend(list_to_add)

    def remove(self, item):
        if item in self:
            print("Removed [{}] from the list".format(item))
            super().remove(item)

    def pop(self, value=None):
        if value is None:
            item = super().pop()
            print(f"Popped [{item}] from the list.")
            return item
        else:
            item = super().pop(value)
            print(f"Popped [{item}] from the list.")
            return item
