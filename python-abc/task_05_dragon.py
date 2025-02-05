#!/usr/bin/python3
"""
5. The Mystical Dragon - Mastering Mixins
"""


class SwimMixin():
    """
    Mixin class
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin():
    """
    Mixin class
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class
    """
    def roar(self):
        print("The dragon roars!")
