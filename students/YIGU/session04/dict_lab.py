# coding=utf-8
# 1
# Create a dict
dict1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
# Display the dictionary.
print dict1
# Delete the entry for "cake"
dict1.pop("cake")
# Display the dictionary.
print dict1
# Add an entry for “fruit” with “Mango” and display the dictionary.
dict1["fruit"] = "Mango"
# Display the dictionary keys.
print dict1.keys()
# Display the dictionary values.
print dict1.values()
# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print "cake" in dict1
# Display whether or not “Mango” is a value in the dictionary.
print "Mango" in dict1.values()

# 2
# Dictionary of numbers from zero to fifteen and the hexadecimal equivalent
dict2 = {}

numbers = range(16)

hexadecimal = []
for i in range(16):
    hexadecimal.append(hex(i))

for i, j in zip(numbers, hexadecimal):
    dict2[i] = j

print dict2

# 3
# Update value for dict1
dict3 = {}
for key in dict1:
    dict3[key] = dict1[key].count(u'a')

# 4
# sets contain numbers from zero through twenty, divisible 2, 3 and 4
s2 = ([])
s3 = ([])
s4 = ([])

for i in range(21):
    if i % 2 == 0:
        s2.append(i)
    if i % 3 == 0:
        s3.append(i)
    if i % 4 == 0:
        s4.append(i)

# 5

pythoni = "python" + "i"
python_set = set(pythoni)
marathon = "marathon"
marathon_fset = frozenset(marathon)

print python_set.union(marathon_fset)
print python_set.intersection(marathon_fset)
