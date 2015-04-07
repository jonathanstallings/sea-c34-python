#!/usr/local/bin/env python

# Section 1
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

user1 = raw_input("What fruit would you like to add to the list? ")
fruit.append(user1)
print(fruit)

user2 = int(raw_input("What index would you like to call from the fruit list? "))
print(fruit[user2 - 1])

fruit = ["Guava"] + fruit
print(fruit)

fruit.insert(0, "Tomatoes")
print(fruit)

for item in fruit:
    if item[0] is "P":
        print item

# Section 2
print(fruit)

del fruit[-1]
print(fruit)

user3 = str(raw_input("What fruit would you like to remove? "))
while user3 not in fruit:
    user3 = str(raw_input("Please select a fruit from the list. "))
else:
    while user3 in fruit:
        fruit.remove(user3)
    print(fruit)

# Section 3
while len(fruit) > 0:
    for item in fruit:
        user4 = raw_input("Do you like " + item.lower() + "? ")
        while user4 != "Yes" and user4 != "No":
            user4 = raw_input("Please enter Yes or No: ")
        else:
            if user4 == "No" or user4 == "no":
                while item in fruit:
                    fruit.remove(item)
                    print(fruit)
            else:
                user4 = raw_input("Do you want to continue? ")
                while user4 != "Yes" and user4 != "No":
                    user4 = raw_input("Please enter Yes or No")
                else:
                    if user4 is "No":
                        break
                print(fruit)
if len(fruit) < 1:
    print("The list is empty!")
else:
    print (fruit)

# Section 4
fruit2 = fruit
print(fruit2)

fruit3 = []

for word in fruit2:
    revWord = word[::-1]
    fruit3.append(revWord)
print(fruit3)

del fruit[-1]
print(fruit)
print(fruit3)
