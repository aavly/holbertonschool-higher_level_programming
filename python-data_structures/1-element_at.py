#!/usr/bin/python3

def element_at(my_list, idx):
    listLength = len(my_list)
    found = 0

    if idx < 0:
        return None

    for i in range(listLength):
        if my_list[i] == idx:
            found = 1
            element = my_list[i + 1]
            break

    if found == 0:
        return None
    else:
        return element
