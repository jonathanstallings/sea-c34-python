#!/usr/bin/python

'''This file outlines examples of four different error functions. Name,
Type, Syntax,and Attribute. Their inputs are either an integer, str, or object.
The functions will produce errors instead of print statements'''


def NameE(a):
    # here we get a name error because we are attempting to access a variable
    # that doesnt exist
    print(y)


def TypeE(b):
    # here we get a type error because we can not perform math on a str object
    b = 2
    print('b' + b)


def SyntaxE(c):
    # we receive this error because we attempt a variable assignment and print
    # statement without the proper syntax
    if c == 7 print(c)


def AttributeE(object):
    # we create this object but receive the error (below) because we are
    # attempting to access an attribute that does not exist.
    class Zero_attributes(object):
        pass

if __name__ == '__main__':

    # Test a name error
    NameE(5)

    # Test a Type error
    TypeE(b)

    # Test a syntax error
    SyntaxE(c)

    # Test Attribute Error

    o = Zero_attributes()
    print o.an_attribute
