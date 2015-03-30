# Exceptions (2 questions)

# Question 1


def age_exception():
    """
    What if I print ask to print a key that isn't in the dictionary?
    Result:
        ValueError: invalid literal for int() with base 10: 'ten'
        (line 15) - when a non integer is entered, "Entry Error." is printed
    """
    while True:
        try:
            x = int(raw_input("How old are you? : "))
            print x
        except ValueError:
            print "Entry error. Please enter your age using numeric values. "
            break

age_exception()


# Question 2


def raise_exception():
    """
    What if you raise an exception?
    Result:
        NameError: NameError raised
        (line 38) - "There is a NameError" is printed to the console

    """
    try:
        raise NameError("NameError raised")
    except NameError:
        print "There is a NameError"

raise_exception()
