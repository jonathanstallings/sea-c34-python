'''Comprehension functions
   Richard Green
   Foundations 2 Python'''

# comprehensions
# list comprehension

import string

z = range(0, 10)

y = range(0, 25, 2)

x = range(0, 25)

a = string.lowercase[:26]


def comp_list(z):
    '''Question: Using Comprehensions what are the results when the equation
    below is applied to a sequence of numbers. Arguments a string with a
    range of numbers'''
    return [2 * x + 50 for x in z]

# nested list comprehension


def comp_nested_list(x, z):
    '''Question: Using Comprehensions and nested loops what are the results of
    the equation that uses numbers divisible by 2 in one sequnece are applied
    to two sequences of numbers. Arguments two numerical sequences'''
    return [i % 2 == 0 for i in x for var in z]

# set comprehension
# Turn a sequence into a set


def set_comp(a):
    '''Question: How do we use comprehensions to convert a (string) sequence of
    characters to a set? Arguments a sequences of characters'''
    new_set = {item for item in a}

    return new_set

if __name__ == "__main__":

    print comp_list(z)

    print comp_nested_list(y, x)

    print set_comp(a)
