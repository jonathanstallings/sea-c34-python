"""What are the different string formatting operators, and how are they
used."""
string1 = "Hello, %s. You have a %d bill? Can you give me %f?" % ("Scott", 20, 1.25)

"""How is the string module used to enhance your code?"""
from string import *  # I'm aware this should not be used universally.

string2 = "I like Grapes!!"

print string.upper(string2)
print string.lower(string2)
print string.join(string.split(string2), "+")
print string.split(string2)
print string.count(string2, "a")
print string.replace(string2, "Grapes", "Bananas")

# upper => I LIKE GRAPES!!
# lower => i like grapes!!
# join => I+like+Grapes!!
# split => ['I', "like", 'Grapes!!']
# count => 1
# replace => I like Bananas!!

"""What's one way to use .format() rather than '%' with strings?"""
li = ["abba", "dabba", "dooo", "bopp", "shibang", "zinger"]
print '{0} {2} {1} {1} {5} {1} {4} {3}'.format(*li)
# abba dooo dabba dabba zinger dabba shibang bopp
