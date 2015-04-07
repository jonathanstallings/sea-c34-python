from __future__ import print_function


def fizz_buzz():
    for x in range(0, 100):
        if (x % 3 == 0) and (x % 5 != 0):
            print(u"Fizz")
        elif (x % 5 == 0) and (x % 3 != 0):
            print(u"Buzz")
        elif (x % 3 == 0) and (x % 5 == 0):
            print(u"FizzBuzz")
        else:
            print(x)

fizz_buzz()