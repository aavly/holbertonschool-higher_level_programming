#!/usr/bin/python3

def best_score(a_dictionary):

    biggest = None

    for key in a_dictionary:
        if a_dictionary[key] > biggest:
            biggest = a_dictionary

    return biggest
