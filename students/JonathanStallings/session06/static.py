import sys
import traceback

# Does a static method within a class have access to class attributes?


class TestStatic(object):
    """A test class with a static method."""
    name = "Foo"

    @staticmethod
    def mult(a, b):
        print(self.name)
        return a * b


try:
    TestStatic.mult(10, 2)
except NameError:
    traceback.print_exc(file=sys.stdout)
else:
    print(TestStatic.name)


# result: As expected, the static method does not have access to class
# properties through self. Python actually throws an error at runtime
# even before attempting the try block.

