# questions about the dictionaries section in slides 4

mydict = {"mary": 20, "josh": 100, "zuleika": 2}


def addtodict(dictname, key, value):
    """
    The question is: can I use a dictionary function to add names for my donor
    list?
    """
    dictname[key] = value
    return dictname

print mydict

addtodict(mydict, "mary", 50)
addtodict(mydict, "cassie", 500)

print mydict


def gettotals(dictname, name):
    """
    Can a dictionary return total value for multiple same keys?
    """
    total = 0
    for x, y in dictname.items():
        if x == name:
            total += y
    return total


marytotal = gettotals(mydict, "mary")
print marytotal

# no because when I add another donation to the dictionary
# it overwrites the one before. so this won't work. python won't tolerate
# multiple identical keys


def getdonationtotals(dictname):
    """
    Let's get a total of all the donations in our database...
    """
    total = 0
    for x in dictname.values():
        total += x
    return total

total = getdonationtotals(mydict)
print "We've raised $%s, that's a lot of donations!" % total


def makeset(list):
    """
    Let's convert a list to a set. Why? Reasons...
    """
    s = set()
    for item in list:
        s.update([item])
    return s

mylist = "apples", "carrots", "oranges"
myset = makeset(mylist)
print myset
print type(myset)
