#!/usr/bin/python3
"""
6. Create object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    Write a function that creates an Object from a “JSON file”:
    """

    with open(filename, 'r', encoding="utf-8") as f:
        obj = json.load(f)
        return obj
