#!/usr/bin/python3
"""
0. Basic Serialization
"""
import pickle


def serialize_and_save_to_file(data, filename):
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    with open(filename, "rb") as file:
        loaded_data = pickle.load(file)
    return loaded_data
