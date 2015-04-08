#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    """Create a circle object."""
    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2
        self._area = math.pi * radius ** 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius
        self._diameter = radius * 2
        self._area = math.pi * radius ** 2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
        self._radius = diameter / 2
        self._area = math.pi * (diameter/2) ** 2

    @property
    def area(self):
        return self._area

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
        if self._area > other._area:
            return 1
        elif self._area < other._area:
            return -1
        else:
            return 0


