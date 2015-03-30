#! /usr/bin/env python

# first series of actions
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print "\n"
print fruit_list
print "\n"

while True:
    add_fruit = raw_input("Add another fruit to the list: ")
    add_fruit = add_fruit.capitalize()
    check_add_fruit = add_fruit in fruit_list
    is_fruit_valid = add_fruit.isalpha()
    if is_fruit_valid is True:
        if check_add_fruit is True:
            print("Sorry, %s is on the list already." % add_fruit)
            print "\n"
        else:
            break
    else:
        print("%s? What's that? \n" % add_fruit)
fruit_list.append(add_fruit)
print fruit_list
print "\n"

while True:
    user_num = int(raw_input("Pick a number 1-5: "))
    if user_num >= 1 and user_num <= 5:
        print("%i) %s" % (user_num, fruit_list[user_num - 1]))
        print "\n"
        break
    else:
        print("Oops! You entered %i." % user_num)
        print "\n"

fruit_list = ["Durian"] + fruit_list
print fruit_list
print "\n"

fruit_list.insert(0, "Lychee")
print fruit_list
print "\n"

counter = 0
check_letter = "P"
print("Fruits that start with the letter \"%s\": " % check_letter)
for fruit in fruit_list:
    if fruit[0] == "P":
        counter += 1
        print("%i) %s" % (counter, fruit))
print "\n"

# second series of actions

print fruit_list
print "\n"
fruit_list.pop()
print fruit_list
while True:
    remove_fruit = raw_input("Which fruit would you like to have removed?: ")
    remove_fruit = remove_fruit.capitalize()
    check_fruit = remove_fruit in fruit_list
    if check_fruit is False:
        print("Sorry, %s is not on the list. \n" % remove_fruit)
    else:
        fruit_list.remove(remove_fruit)
        break
print "\n"
print fruit_list
print "\n"

# third series of actions

counter = 0
while(counter < len(fruit_list)):
    fruit_list[counter] = fruit_list[counter].lower()
    counter += 1

print fruit_list
print "\n"

counter = 0
list_len = len(fruit_list)
while(counter < list_len):
    user_resp = raw_input("Do you like %s? " % fruit_list[counter])
    user_resp = user_resp.lower()
    if user_resp == "no":
        fruit_list[counter] = "remove"
        counter += 1
    elif user_resp == "yes":
        counter += 1
    else:
        print "Oops! You must enter \"yes\" or \"no\"."

while True:
    check_remove = "remove" in fruit_list
    if check_remove is True:
        fruit_list.remove("remove")
    else:
        break

print fruit_list
print "\n"

# last series of actions

fruit_list_copy = fruit_list[:]
counter = 0
while(counter < len(fruit_list_copy)):
    fruit_list_copy[counter] = fruit_list_copy[counter][::-1]
    counter += 1

fruit_list.pop()
print fruit_list
print "\n"
print fruit_list_copy
print "\n"
