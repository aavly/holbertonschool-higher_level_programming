#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary == None:
        return None

    # access first key and assign to biggest
    biggest = next(iter(a_dictionary.values()))

    for key in a_dictionary:
        if a_dictionary[key] > biggest:
            biggest = a_dictionary

    return a_dictionary.get(biggest)
