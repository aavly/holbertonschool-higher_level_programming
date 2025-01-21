#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    for key in sorted(a_dictionary.keys()):
        a_dictionary[key] = a_dictionary[key] * 2
        print(f"{key}: {a_dictionary[key]}")
