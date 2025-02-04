#!/usr/bin/python3
"""Creating an abstract class and two subclasses"""


from abc import ABC, abstractmethod
import math


# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Concrete subclasses
class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius**2)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return (2 * self.__height) + (2 * self.__width)



def shape_info(obj):
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))


# Testing
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)
