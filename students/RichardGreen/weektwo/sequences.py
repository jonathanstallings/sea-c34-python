#!/usr/bin/python

x = 'this is my string. how do you like it'
z = 'how'
p = 'good morning!'

'''Im going to define three separate functions to answer questions about the'''
'''strings above. My questions:'''
'''How long is my sequence?/what are its first three characters?'''
'''What will concatenating strings together look like?'''
'''Are these characters in my string?'''


def lengthofstring(x):
    '''definition of function: find the length of the string'''
'''arguments: a string'''
print " The length of the string is:"
print len(x)
print "The first three characters of the string are:"
print x[0:2]


def concatenatestrings(p, x):
    '''definition of function: add two strings together'''
'''arguments: a string'''
summed_string = p + x
print "your summed string is:"
print summed_string


def isitinmystring(x, z):
    '''definition of function: determine if my characters are in a string'''
'''arguments: a substring x and the master string y'''
if z in x:
    print " Yes your character(s) ' %s '' is in the string" % (z)
else:
    print " No, your character is not in the string"

if __name__ == "__main__":
    lengthofstring(x)
    concatenatestrings(p, z)
    concatenatestrings(p, x)
