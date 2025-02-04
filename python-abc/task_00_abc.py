#!/usr/bin/python3
"""Creating an abstract class and two subclasses"""


from abc import ABC, abstractmethod


# Abstract class
class Animal(ABC):

    # Abstract method
    @abstractmethod
    def sound(self):
        pass


# Concrete subclasses
class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
