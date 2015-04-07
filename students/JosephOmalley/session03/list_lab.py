#!/usr/bin/env python
"""JosephO'Malley"""
"""Session 3 task6"""

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print fruit_list
new_fruit = raw_input("What fruit would you like to add?")
fruit_list.append(new_fruit)
print fruit_list
number = int(raw_input("Please provide a number between 0 and 4"))
print ("Your number is %s and the corresponding fruit is %s." % (number, fruit_list[number]))
fruit_list = ["Mangos"] + fruit_list
print fruit_list
fruit_list.insert(0, "Kiwis")
print fruit_list
for fruits in fruit_list:
    if fruits[0] == "P":
        print fruits
print fruit_list
fruit_list.pop()
print fruit_list
delete_fruit = raw_input("What fruit would you like to remove?")
deleting = True
while deleting:
    if delete_fruit in fruit_list:
        fruit_list.remove(delete_fruit)
        deleting = False
    else:
        delete_fruit = raw_input("That fruit is not in the list. Try again.")
print fruit_list
choosing = True
while choosing:
    delete_list = list(fruit_list)
    for fruits in fruit_list:
        choice = raw_input("Do you like %s? 'Yes' or 'No'?" % (fruits))
        if choice == "No":
            delete_list.remove(fruits)
            choosing = False
        elif choice == "Yes":
            choosing = False
        else:
            choice = raw_input("That is not a correct response. 'Yes' or 'No'")
print delete_list
list_copy = [] 
for copies in delete_list:
    list_copy.append(copies[::-1])
print list_copy



