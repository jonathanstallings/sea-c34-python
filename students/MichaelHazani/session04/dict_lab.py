# Task 9 part 1:

dictionary = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

print dictionary
del dictionary['cake']
print dictionary

dictionary['fruit'] = 'Mango'

print dictionary
print dictionary.keys()
print dictionary.values()
print('cake' in dictionary.keys())
print('Mango' in dictionary.values())


# Task 9 part 2:

regnum = range(15)

hexnum = []
for x in regnum:
    hexnum.append(hex(regnum[x]))
numhex = dict(zip(regnum, hexnum))
print numhex


# Task 9 part 3:

dictionary = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
valuelist = list(dictionary.values())
keyslist = list(dictionary.keys())
aoccurence = []

for x in valuelist:
    aoccurence.append(x.count('a'))

dictionary2 = dict(zip(keyslist, aoccurence))
print dictionary2


# Task 9 part 4:
s2 = set()
s3 = set()
s4 = set()

for x in range(20):
    if x % 2 == 0:
        s2.add(x)
    if x % 3 == 0:
        s3.add(x)
    if x % 4 == 0:
        s4.add(x)

print s3.issubset(s2)
print s4.issubset(s2)


# Task 9 part 5:

pythonset = set(['p', 'y', 't', 'h', 'o', 'n'])
pythonset.add('i')
marathonset = frozenset(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])
print pythonset.union(marathonset)
print pythonset.intersection(marathonset)
