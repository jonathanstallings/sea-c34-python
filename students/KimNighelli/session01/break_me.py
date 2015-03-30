import datetime
#I use datetime all the time at work to deal with date format and timezone issues.

def syntax_error(some_date, some_fmt):
    return datetime.strptime()

def attribute_error(some_date, some_fmt):
    return datetime.strpptime()

def type_error(string, some_float):
    return string + some_float

def name_error():
    return x

####Syntax Error######
# A syntax error occurs when Python syntax is incorrect. The syntax
# below is incorrect in the fmt block, there should not be three quotes.

#syntax_error("2015-03-16", "%Y-"%m-%d")

#Error Received:
#  File "break_me.py", line 19
#    syntax_error("2015-03-16", "%Y-"%m-%d")
#                                       ^
#SyntaxError: invalid syntax


####Attribute Error####
# This arises when an attribute asignment fails. In this case, the
# function is wrong. The module datetime has an attribute "strptime",
# I spelled it incorrectly above. datetime.strpptime does not exist!

#attribute_error("2015-03-16", "%Y-%m-%d")

#Error Received:
#  File "break_me.py", line 8, in attribute_error
#    return datetime.strpptime()
#AttributeError: 'module' object has no attribute 'strpptime'


#### Type Error ####
# If an operation is not supported on a variable's type, a type
# error is raised, Below, I try to add a string and float.

#type_error("String!", 11.13)

#Error Received:
#File "break_me.py", line 11, in type_error
#    return string + some_float
#TypeError: cannot concatenate 'str' and 'float' objects


### Name Error ###
# Occurs when a variable cannot be found because it's not defined.
# Below, I never defined x

print name_error()

# File "break_me.py", line 14, in name_error
#    return x
#NameError: global name 'x' is not defined
