from __future__ import print_function
import sys
import traceback


def for_test():
    """What happens when the for-block changes the iterator?"""
    for x in range(10):
        print(x)
        x = 20
    else:
        print(u"Loop finished! x is {x}.".format(x=x))


# for_test()
# result: The for loop iteration process is not disturbed.


def continue_test():
    """Will continue prevent the following break and return statements?"""
    for x in range(1, 10):
        if not x % 3:
            continue
            break
            return u"fizz"
        elif not x % 6:
            break
        else:
            print(x)
    else:
        print(u"Loop finished! x is {x}.".format(x=x))


# continue_test()
# result: Absolutely.


def index_test():
    """
    What happens if I add another symbol to the example construct
    from the session03 notes about adding an index to for loops ?
    """
    try:
        for i, j, foo in enumerate(u'Python'):
            print(i, j, foo, end=' ')
    except:
        print(u'This construct caused an exception.')
        traceback.print_exc(file=sys.stdout)

# index_test()
# result: Apparently this modifcation causes a ValueError.
