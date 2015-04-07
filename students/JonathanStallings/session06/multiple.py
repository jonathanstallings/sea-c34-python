# How do the various inits combine when called to a subclass with
# multiple inheritance?


class Super1(object):
    """Init Super1."""
    def __init__(self, x):
        self.x = x


class Super2(object):
    """Init Super2"""
    def __init__(self, y):
        self.y = y


class Super3(object):
    """Init Super 3."""
    def __init__(self, z):
        self.z = z


class SubClass(Super1, Super2, Super3):
    """Init Subclass with multiple inheritance."""
    def __init__(self, name, x, y, z):
        self.name = name
        Super1.__init__(self, x)
        Super2.__init__(self, y)
        Super3.__init__(self, z)


Sub = SubClass("Yellow", 10, 10, 50)
print(
    u"My name is {name}, and my coordinates are {x}, {y}, {z}."
    .format(name=Sub.name, x=Sub.x, y=Sub.y, z=Sub.z)
)

# result: As long as the appropriate arguments are passed from SubClass
# init into respective superclass inits, all is well.

