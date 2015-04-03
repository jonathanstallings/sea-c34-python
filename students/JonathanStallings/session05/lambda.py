from __future__ import print_function


def function_builder(n):
    """
    Return a list of n functions that return input
    incremented by increasing number.
    """
    return [lambda x, i=i: x+i for i in range(n)]


the_list = function_builder(4)
assert(the_list[0](2) == 2)
assert(the_list[1](2) == 3)
for f in the_list:
    print(f(5), end=" ")

