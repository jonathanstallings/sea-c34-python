#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    """Create a circle object."""
    def __init__(self, radius):
        self._radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2

    def __str__(self):
        return (
            u"Circle with radius: {:.6f}"
            .format(float(self._radius))
        )

    def __repr__(self):
        return(
            u"Circle({r})"
            .format(r=int(self._radius))
        )

    def __add__(self, other):
        return Circle(self._radius + other._radius)

    def __mul__(self, mult):
        return Circle(self._radius * mult)

    def __cmp__(self, other):
        if self.area > other.area:
            return 1
        elif self.area < other.area:
            return -1
        else:
            return 0

