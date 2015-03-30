def ordinal_value():
    """
    1. What's the ordinal values of my name: Karen?
    """

    for i in "Karen":
        print(ord(i))


def greetings():
    """
    2. How to create a greeting using the __format__() method?

    """
    name = "Peter"
    print("{}, you have a cool name".format(name))


def string_split():
    """
    3. How to break up strings into a string arrany?
    """

    word = "I have school today"
    word.split(" ")
