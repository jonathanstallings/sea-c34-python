#!/usr/bin/env python


def print_series_header(series_num):
    """Print a header for each list lab series output, to aid in reading."""

    print(u"-------------------")
    print(u"List Lab - Series {}".format(series_num))
    print(u"-------------------")


def print_fruitlist(series_num, step_num, fruitlist):
    """Print the current state of the fruit list as a formatted string
    with the series and step of the lab involved.
    """

    print(u"{}.{} - Current Fruit List: {}"
          .format(series_num, step_num, fruitlist))


def series1():
    """Perform List Lab Series 1 operations."""

    print_series_header(1)
    fruitlist = [u"Apples", u"Pears", u"Oranges", u"Peaches"]
    print_fruitlist(1, 1, fruitlist)

    fruitlist.append(raw_input(u"Enter another fruit: ").capitalize())
    print_fruitlist(1, 2, fruitlist)

    input_num = int(raw_input(u"Enter a number: "))
    if 1 <= input_num <= len(fruitlist):
        chosen_fruit = fruitlist[input_num - 1]
    else:
        chosen_fruit = u"non-existent"

    print(u"1.3 - The number %i fruit in the list is %s."
          % (input_num, chosen_fruit))

    fruitlist = [u"Papaya"] + fruitlist
    print_fruitlist(1, 4, fruitlist)

    fruitlist.insert(0, u"Watermelon")
    print_fruitlist(1, 5, fruitlist)

    for fruit in fruitlist:
        if fruit.startswith(u"P"):
            print(u"1.6 - Fruits that start with P: {}".format(fruit))

    return fruitlist


def series2(fruitlist):
    """Perform List Lab Series 2 operations."""

    print(print_series_header(2))
    print_fruitlist(2, 1, fruitlist)
    fruitlist.pop()
    print_fruitlist(2, 2, fruitlist)
    while True:
        input_fruit = raw_input("2.3 - Enter a fruit to remove: ")
        if input_fruit in fruitlist:
            fruitlist.remove(input_fruit)
            break
    print_fruitlist(2, 4, fruitlist)


def series3(fruitlist):
    """Perform List Lab Series 3 operations."""

    print_series_header(3)
    for fruit in fruitlist[:]:
        answer = ""
        while answer != "yes" and answer != "no":
            answer = raw_input("3.1 - Do you like {}? (enter yes or no): "
                               .format(fruit.lower()))

        if answer == "no":
            fruitlist.remove(fruit)

    print_fruitlist(3, 2, fruitlist)


def series4(fruitlist):
    """Perform List Lab Series 4 operations."""

    print_series_header(4)
    reversed_list = [fruit[::-1] for fruit in fruitlist]
    fruitlist.pop()
    print("4.1 - Original List: {}".format(fruitlist))
    print("4.2 - Reversed List: {}".format(reversed_list))


if __name__ == "__main__":
    fruitlist = series1()
    series2(fruitlist[:])
    series3(fruitlist[:])
    series4(fruitlist[:])