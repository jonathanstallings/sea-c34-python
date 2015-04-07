# part 1
d = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print d
del d["cake"]                        # remove cake from dictionary
print d
d.update({"fruit": "Mango"})  # add mango to dictionary
print d
print d.keys()                           # print all dictionary keys
print d.values()                        # print all dictionary values
print 'cake' in d                        # true if cake is key in dictionary
for key, value in d.iteritems():  # true if Mango is value in dictionary
    if value == "Mango":
        print True

# part 2
numberd = {}
nums = []
for i in range(16):
        nums.append(i)
hex = map(lambda x: hex(x), range(10))
# combine lists nums and hex to create key value pairs in numberdict
for i, j in zip(nums, hex):
    numberd.update({i: j})
print numberd

# part 3
# makes new dict with the numbers of 'a' in value as the new value
a_d = {}
for key, value in d.iteritems():
    a_d.update({key: value.count('a')})

# part 4
s2 = set(filter(lambda x: x % 2 == 0, range(21)))
s3 = set(filter(lambda x: x % 3 == 0, range(21)))
s4 = set(filter(lambda x: x % 4 == 0, range(21)))
print s2
print s3
print s4
print s3.issubset(s2)
print s4.issubset(s2)

# part5
python = set(['P', 'y', 't', 'h', 'o', 'n'])
python.add('i')
marathon = frozenset(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])
# prints all letters python and marathon do not have in common
print python.union(marathon)
# prints all letters python and marathon do have in common
print python.intersection(marathon)
