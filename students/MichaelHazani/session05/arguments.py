def tupleexperiment(x=0):
    """can you pass a tuple inside a kwarg, which is a dict?"""
    return x

x = (4, 3, 4, 5, 6)
# print tupleexperiment(x)
# result: yes


def ambiguousarguments(b):
    """What if you don't specift kwargs as such but still pass them?"""
    return b

dictionary = {1: u'A', 2: u'B', 3: u'C'}

# print ambiguousarguments(dictionary)
# result: dictionary is printed! Python is super flexible!


def wrongarg():
    """what if the format method gives the wrong kind of arg?"""
    d = {u'First': u'A', u'Second': u'B', '3': u'C'}
    print u"if this works you'll see valus from dict:"
    print u"{First} {Second}".format(*d)

wrongarg()
# result: "KeyError: u'First'"" must have ** if you're passing kwarg!
