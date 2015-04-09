# If python properties are defined with the @properties decorator, which
# docstring will be returned by .__doc__?


class PropClass(object):
    """A test class @properties decorator."""
    def __init__(self, x):
        """A test init docstring."""
        self._x = x

    @property
    def x(self):
        """A test docstring under @property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


foo = PropClass(10)
print(foo._x)
print(foo._x.__doc__)

# result: The docstring under @property is not accessible in this way.

