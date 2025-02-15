#!/usr/bin/python3
"""
1. Pickling Custom Classes
"""
import pickle


class CustomObject():
    """
    CustomObject class
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization Error: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)  # Corrected to load from file
        except Exception as e:
            print(f"Deserialization Error: {e}")
            return None
