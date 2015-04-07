#!/usr/bin/env python

my_list = ["Apples", "Pears", "Oranges", "Peaches"]
my_list = ["Bananas"] + my_list
print(my_list)


def user_input():
    fruit_input = raw_input("Give me a fruit to add to our list:")

    my_list.append(fruit_input)

    print(my_list)

    number_input = raw_input("Enter a number:")

    print(number_input)

    number_input = int(number_input)

    print(my_list[(number_input - 1)])

    my_list.insert(0, "Pineapple")

    print(my_list)

    for fruit in my_list:
        if fruit[0] == "P":
            print fruit

user_input()

print(my_list)

del my_list[-1]

print(my_list)


def remove_fruit():
    remove_input = raw_input("Which fruit would you like to remove?:")

    for fruit in my_list:
        if fruit.lower() == remove_input.lower():
            my_list.remove(fruit)

    print(my_list)

remove_fruit()


def user_preference():
    my_tuple = tuple(my_list)

    for fruit in my_tuple:
        while True:
            user_preference = raw_input("Do you like %s :" % fruit.lower())
            if user_preference.lower() == "yes" or user_preference.lower() == "no":
                break
            else:
                print("Only enter 'yes' or 'no'")
        if user_preference.lower() == "no":
            my_list.remove(fruit)
    print(my_list)

user_preference()


list_copy = my_list[:]


def reverse_letter(copy):
    swapped = ""
    for fruit in reversed(copy):
        swapped += fruit[::-1] + " "
    print(swapped)

reverse_letter(list_copy)

del(my_list[-1])

print(my_list)

print(list_copy)
