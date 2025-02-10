#!/usr/bin/python3
"""
5. Save Object to a file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write a function that writes an Object to a text
    file, using a JSON representation:
    """
    return json.dump(my_obj, filename)
