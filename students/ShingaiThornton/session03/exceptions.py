# Q1 How to use try except?


def userdictionary():
    """
    Ask users to add a number to a dictionary.
    Return error message if they enter a non-numeric value

    Args:

    Returns: Dictionary or string
    """
    d = {}

    try:
        d['first'] = raw_input('Enter a number: ')
        print d
    except IOError:
        print("You were supposed to enter a number!")

userdictionary()


# Q2 How to use the finally clause?

def userdictionary2():
    """
    Ask user to enter a number. Return error message if non-numeric.
    Print dictionary even if nothing added.

    Args:

    Returns: Dictionary or string
    """

    d = {}

    if d == {}:
        try:
            d['first'] = int(raw_input('Enter a number: '))
            print("Great!")
        except IOError:
            print(" You were supposed to enter a number, now there's an empty dictionary!")
        finally:
            print d

userdictionary2()
