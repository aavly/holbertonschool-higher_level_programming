#!/usr/bin/python3

def uniq_add(my_list=[]):

    unique_list = []
    unique_sum = 0

    for i in range(len(my_list)):
        if my_list[i] not in unique_list:
            unique_list.append(my_list[i])

    for i in range(len(unique_list)):
        unique_sum += unique_list[i]

    return unique_sum
