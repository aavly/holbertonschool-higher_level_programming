#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = len(my_list) * [None]

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False

    return new_list
