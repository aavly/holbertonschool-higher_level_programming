#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    copy_dictionary = a_dictionary.copy()

    for key in sorted(a_dictionary.keys()):
        copy_dictionary[key] = a_dictionary[key] * 2

    return copy_dictionary
