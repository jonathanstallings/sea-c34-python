# Step 1

people = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "Chocolate"
}

print people

# Delete the key "cake" from the dictionary
people.pop("cake")

print "\n"
print people

# Add an entry for “fruit” with “Mango” and display the dictionary
people["fruit"] = "Mango"

# Display the dictionary keys.
print "\n"
print "Keys in the dictionary People:"
for key in people:
    print key

# Display the dictionary values.
print "\n"
print "Values in the dictionary People:"
for value in people:
    print people[value]

# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print "\n"
desired_key = "cake"
print("Is \"%s\" a key in the dictionary?: " % desired_key)
print desired_key in people

# Display whether or not “Mango” is a value in the dictionary.
print "\n"
desired_value = "Mango"
print("Is \"%s\" a value in the dictionary?: " % desired_value)
print desired_value in people.values()


# Step 2

# Using the dict constructor and zip, build a dictionary of numbers from zero
# to fifteen and the hexadecimal equivalent (string is fine)
nums_dict = {}
nums_list = []
hexadec_list = []
total_numbers = 15

for i in range(total_numbers + 1):
    nums_list.append(i)
    hexadec_list.append(hex(i))

nums_dict = dict(zip(nums_list, hexadec_list))

"""
# Here's a more efficient way to create the dictionary without zip
nums_dict = {}
for i in range(16):
    nums_dict[i] = hex(i)

print nums_dict
"""

# Step 3

# Using the dictionary from item 1: Make a dictionary using the same keys but
# with the number of ‘a’s in each value.

for key in people:
    people[key] = people[key].count('a')

# Step 4

# Create sets s2, s3 and s4 that contain numbers from zero through twenty
# s2 is numbers divisible by 2
# s3 is numbers divisible by 3
# s4 is numbers divisible by 4

s2 = []
s3 = []
s4 = []
total_numbers = 20
for i in range(total_numbers + 1):
    if i % 2 == 0:
        s2.append(i)
    if i % 3 == 0:
        s3.append(i)
    if i % 4 == 0:
        s4.append(i)

s2 = set(s2)
s3 = set(s3)
s4 = set(s4)

print s2
print s3
print s4

# Display if s3 is a subset of s2 (False)
print "\n"
print "Is s3 is a subset of s2? :"
print s3.issubset(s2)

# Display if s4 is a subset of s2 (True)
print "\n"
print "Is s4 is a subset of s2? :"
print s4.issubset(s2)

# Step 5

# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
python_set = set(['P', 'y', 't', 'h', 'o', 'n'])
python_set.add('i')

# Create a frozenset with the letters in ‘marathon’
marathon_set = frozenset(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])

# Display the union and intersection of the two sets.
print "\n"
print "The union of the two sets:"
print python_set.union(marathon_set)
print "\n"
print "The intersection of the two sets:"
print python_set.intersection(marathon_set)
