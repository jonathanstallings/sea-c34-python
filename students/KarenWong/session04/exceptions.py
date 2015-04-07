def divide(a, b):
    """ What happens if you try to catch a different exception
    than the exception that it actually raise?"""
    try:
        a / b
    except IOError as the_error:
        print "An IOError has occurred."
        print the_error
# since the IOError didn't happen, it just raises the zeroDivisionError.


def divide_parttwo(a, b):
    """ What happens to the finally block if the error raises before the
    function it gets there?"""
    try:
        a / b
    except ZeroDivisionError as the_error:
        print "An ZeroDivisionError has occurred."
        print the_error
    finally:
        return 2
# the function will still run and return 2.

divide(1, 0)
divide_parttwo(1, 0)
