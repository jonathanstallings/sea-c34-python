# How is a List of Tuples organized and accessed using a For Loop?
listTuple = [("rabbit", 10), ("donkey", 2), ("frog", 4)]
for animal, qty in listTuple:
    print("I have a %s, and there are %d others nearby." % (animal, qty))

# Does the above example effect mutability given Lists are mutable and
# Tuples are not?
listTuple[0] = ("bee", 1000)
print listTuple[0]

# This is something I think would work for a side project I was working
# on before class started: Scrabble Cheater. It takes command line arguments
# in the for of letters, "abileslic" for example, and checks them against
# the SOWPODS.txt dictionary. It returns word options to play with
# corresponding scores.
# I broke the argument up using list(). Could I have just used tuple() to
# create individual string characters?

rack = "isleidser"
newRack = tuple(rack)
for item in newRack:
    print item  # I would do something else here, but just keeping it simple
