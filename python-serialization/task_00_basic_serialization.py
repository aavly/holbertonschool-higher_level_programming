#!/usr/bin/python3
"""
0. Basic Serialization
"""
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    with open(filename, "r") as file:
        loaded_data = json.load(file)
    return loaded_data
