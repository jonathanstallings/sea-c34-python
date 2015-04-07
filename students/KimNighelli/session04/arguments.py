'''
This is for Task 12- Exploring Session 5- Arguments

The following functions were written to help clarify some
questions and misunderstandings I had while reviewing the
session 5 lecture notes. Each question will be noted by a
comment line #

Kimberlee Nighelli - 30 March 2015
'''

import copy

# Question 1: To better understand how to use keyword arguments,
# can I calculate the area of a triangle using keyword arguments?


def area_triange(base=0, height=0):
    '''
    Calculate the area of a triange where A = 1/2 * b * h
    '''
    area = 0.5 * base * height
    print "The area of a triange with base %f and height %f is %f \
            " % (base, height, area)

    return area

# Question 2: To betterunderstand how to use .format(), can I create a
# string that holds various weather data using keyword arguments?


def format_method(**kwargs):
    '''
    Create a weather descriptor string using keyword arguments
    '''

    print "The weather on {day} will be {descriptor} with a " \
          "high temperature of {temperature}".format(**kwargs)


# Question 3: What is the difference between a shallow and deep copy?

def copy_types(list_a):
    '''
    Performs the same action on both a shallow copy and deep
    copy of the input list. By printing both, I should be able
    to see the difference
    '''

    print "\nOriginal list, list_a: ", list_a

    # Shallow copy
    list_b = copy.copy(list_a)

    list_a[2].append('London')
    print "\nList_a after appending: ", list_a
    print "Copied list_b after appending: ", list_b

    # Although I tried to append 'London' to the
    # original list, the city was appended to both.

    # Deep copy
    list_c = copy.deepcopy(list_a)
    list_a[0].append('peach')

    print "\nList_a, after appending a fruit: ", list_a
    print "List_c, a deep copy of list_a: ", list_c

    # Unlike with the shallow copy, 'Peach was only appended
    # to the original list.

if __name__ == "__main__":
    MEASUREMENTS = {"base": 3, "height": 4}
    area_triange(**MEASUREMENTS)

    WEATHER = {"day": "Tuesday", "descriptor": "rainy", "temperature": 61}
    format_method(**WEATHER)

    LIST_A = [['apple', 'banana', 'mango'], [9, 8, 7, 6],
              ['Seattle', 'Boston', 'Stockholm']]
    copy_types(LIST_A)
