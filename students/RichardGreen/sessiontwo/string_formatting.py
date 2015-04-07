#!/usr/bin/python

s = 'this is my string. how do you like it'
x = u"25.4, 56.1, 12.9"
name = 'Rich'
age = '35'
home = "Hamden, CT"

'''Im going to define three separate functions to answer questions about'''
'''string functions. My questions:'''
'''Are the values in my string alphanumeric?'''
'''How can I split my data up from comma to tab delimited'''
'''How do you say good morning in english, spanish, and swedish?'''
'''Write a program that takes in a name and says good morning in'''
'''three languages'''


def is_it_alpha_num(x):
    '''definition of function: Determnine if the string has alphanumeric'''
'''characters'''
'''arguments: a string'''
# x = str(x)
if x.isnumeric() and x.isalpha():
    print "Yes these are alpha numeric characters"
if x.isnumeric() and not x.isalpha():
    print "These are numeric characters"
if x.isalpha() and not x.isnumeric():
    print "Yes these are alphabetic characters"
else:
    print "These do not appear to be alphanumeric characters"


def split_a_string(x):
    '''definition of function: Split a string by commas,replace with tabs'''
'''arguments: a string'''
s_split = x.split(', ')
tsv = '\t'.join(x.split(', '))
print "your new string is:"
print tsv


def good_morning(name, age, home):
    '''definition of function: Introducing yourself'''
'''arguments: 3 strings'''
age = int(age)
if not name:
    print "please enter a name, age, and hometown"
else:
    print "Hello %s, Good Morning" % (name)
    print "I see you are %d and from %s" % (age, home)


if __name__ == "__main__":
    is_it_alpha_num(s)
    is_it_alpha_num(x)
    split_a_string(s)
    good_morning(name, age, home)
