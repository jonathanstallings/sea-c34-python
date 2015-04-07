#!/usr/bin/env python

from __future__ import print_function


fruits = []


def display(l):
    """
    Display a list as a formatted string.

    Args:
        l: the list to be displayed.
    """
    list_str = ', '.join(l)
    print('\n' + list_str)


def series_1():
    """First series"""
    global fruits
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    msg = ""

    print(u'\n\nSeries 1:\n\n')
    display(fruits)

    msg = u'\nPlease enter an additional type of fruit.\n\n>  '
    fruits.append(raw_input(msg).title())
    display(fruits)

    msg = u'\nPlease enter a number between 1 and {length}.\n\n>  ' \
        .format(length=len(fruits))
    num = raw_input(msg)
    print(num + ". " + fruits[int(num) - 1])

    fruits = ['Blueberries'] + fruits
    display(fruits)

    fruits.insert(0, "Snozberries")
    display(fruits)

    p_fruits = []
    for fruit in fruits:
        if fruit[0] == 'P':
            p_fruits.append(fruit)
    display(p_fruits)

    return fruits


def series_2():
    """Second series"""
    fruits_2 = fruits[:]
    response = ""

    print(u'\n\nSeries 2:\n\n')
    display(fruits_2)
    fruits_2.pop()
    display(fruits_2)
    fruits_2.extend(fruits_2)

    msg = u'\nPlease enter a fruit to delete.\n\n>  '
    while response not in fruits_2:
        display(fruits_2)
        response = raw_input(msg).title()
    while response in fruits_2:
        fruits_2.remove(response)
    display(fruits_2)

    return fruits_2


def series_3():
    """Third Series"""
    fruits_3 = fruits[:]

    print(u'\n\nSeries 3:\n\n')
    for fruit in fruits_3[:]:
        msg = u'\nDo you like {fruit}? ([Y]es/[n]o):\n\n>  ' \
            .format(fruit=fruit.lower())
        while True:
            response = raw_input(msg).lower()
            if response == 'yes' or response == 'y':
                break
            elif response == 'no' or response == 'n':
                fruits_3.remove(fruit)
                break
    display(fruits_3)

    return fruits_3


def series_4():
    """Fourth Series"""
    fruits_4 = []

    print(u'\n\nSeries 4:\n\n')
    for fruit in fruits[:]:
        fruits_4.append(fruit[::-1])
    fruits.pop()
    display(fruits)
    display(fruits_4)

    return fruits_4


if __name__ == '__main__':
    series_1()
    series_2()
    series_3()
    series_4()
