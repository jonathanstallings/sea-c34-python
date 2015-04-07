#!/usr/bin/python

'''Outlined below are a series of list functions and commands'''

'''Session 1'''
# Create a list that contains .Apples., .Pears., .Oranges. and .Peaches..
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches'];
# Display the list.
print " The fruit we have is:", fruit
# Ask the user for another fruit and add it to the end of the list.
new_fruit = 'pears'#raw_input('Enter your Fruit: ')
print "Adding", new_fruit
# add to list
fruit.append(new_fruit)
# Display the list.
print " Our updated fruit list is:", fruit
# Ask the user for a number and display the number back to the user and the
# fruit corresponding to that number (on a 1-is-first basis).
location = '3' # raw_input('Enter a number: ')
print('You entered', location)
if int(location) <= len(fruit):
    print "The fruit at your number is:", fruit[int(location)]
else:
    print " Im sorry the location you entered is incorrect."

# Add another fruit to the beginning of the list using .+. and display the list
fruit = ["cherries"] + fruit
print "Our updated fruit list is:", fruit
# Add another fruit to the beginning of the list using insert() and displaylist
fruit.insert(1, "blueberries")
print " Our updated fruit list is:", fruit
# Display all the fruits that begin with .P., using a for loop.
for item in fruit:
    if item.startswith("P"):
        print item
'''Session 2'''
# Display the list.
print " Our fruit list is:", fruit
# Remove the last fruit from the list.
del fruit[len(fruit) - 1]
# Display the list.
print " Our updated fruit list is:", fruit
# Ask the user for a fruit to delete and find it and delete it.
del_fruit = 'cherries'  # raw_input('Enter your Fruit: ')
fruit.remove(del_fruit)
print " Our updated fruit list is:", fruit
'''Session 3'''
# Ask the user for raw_input displaying a line like .Do you like apples?.
print "Do you like ?", fruit[0]
response = 'yes'  # raw_input('Enter: yes or no ')
count = len(fruit) - 1
while count > 0:
    if response == 'yes':
        print " Thanks glad you like", fruit[count].lower()
        count = count - 1
        print "Do you like ?", fruit[count]
        response = 'yes'  # raw_input('Enter: yes or no ')
    if response == 'no':
        print " OK. I will remove it then", fruit.remove(fruit[count])
        count = count - 1
        print "Do you like ?", fruit[count]
        response = 'no'  # raw_input('Enter: yes or no ')
    else:
        print "please respond with either yes or no in lower case. Thanks"

# For each no., delete that fruit from the list.
# For any answer that is not .yes. or .no., prompt the user to answer with one
# of those two values (a while loop is good here):
# Display the list.
print " Our updated fruit list is:", fruit
'''Session 4'''
# Make a copy of the list and reverse the letters in each fruit in the copy.
fruit2 = fruit[:]
print(fruit2[:-1])

# Delete the last item of the original list.
# Display the original list and the copy.
fruit = fruit[::-1]
print " Our original fruit list is:", fruit
print " Our copied fruit list is:", fruit2
