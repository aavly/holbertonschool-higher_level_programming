#!/usr/bin/python3
"""
4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
"""

class Fish():
    """
    Parent class Fish
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird():
    """
    Parent class Bird
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class that inherits from both a Fish and a Bird class.
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
