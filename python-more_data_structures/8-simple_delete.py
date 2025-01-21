#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    
    for key in a_dictionary:
        if key:
            a_dictionary.pop(key)

    return a_dictionary
