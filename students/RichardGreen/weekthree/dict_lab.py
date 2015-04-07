'''Dictionary Set Lab'''
'''Richard Green'''
'''Session 05'''

my_dict = {"name": 'Chris',
           "city": 'Seattle',
           "cake": 'Chocolate'}

# Display the dictionary.

print my_dict

# Delete the entry for cake

my_dict.pop('cake')

# Display the dictionary.

print my_dict


# Add an entry for fruit with Mango and display the dictionary

my_dict.update({'fruit': 'Mango'})

# Display the dictionary.

print my_dict


# Display the dictionary keys.

print my_dict.keys()

# Display the dictionary values.

print my_dict.values()

# Display whether or not cake is a key in the dictionary (i.e. False) (now)

if 'cake' in my_dict.itervalues():
    print True
else:
    print False

# # Display whether or not Mango is a value in the dictionary.

if 'Mango' in my_dict.itervalues():
    print True
else:
    print False

# Using the dict constructor and zip, build a dictionary of numbers
# from zero to fifteen and the hexadecimal equivalent (string is fine).

# I decided to use lists so I can append the values back to them
l1 = []
l2 = []

# I need to iterate through each value to convert to hexadecimal
for i in range(0, 16):
    l1.append(i)
    l2.append(hex(i))

new_hexs_dict = dict(zip(l1, l2))
print new_hexs_dict


####
# Using the dictionary from item 1: Make a dictionary using
# the same keys but with the number of as in each value.
#

my_a_dict = dict()

for k, v in my_dict.iteritems():
        try:

            my_a_dict[k] = v.count('a')

        except TypeError:
            pass
print "The number of [a]s in the dictionary are:"
print my_a_dict


# Create sets s2, s3 and s4 that contain numbers from zero through twenty,
# divisible 2, 3 and 4.

s2 = set()
s3 = set()
s4 = set()

for i in range(0, 20):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)
    else:
        pass

# Display the sets.
print "The contents of s2 are:"
print s2
print "The contents of s3 are:"
print s3
print "The contents of s4 are:"
print s4


# Display if s3 is a subset of s2 (False)

if s3.issubset(s2):
    print True
else:
    print False

# Display if s4 is a subset of s2 (True).
if s4.issubset(s2):
    print True
else:
    print False

# Create a set with the letters in Python and add i to the set.

py_set = set('Python')

py_set.add('i')

print py_set

# Create a frozenset with the letters in marathon
fs = frozenset(('marathon'))

print fs

# Display the union and intersection of the two sets.

print py_set.union(fs)

print py_set.intersection(fs)
