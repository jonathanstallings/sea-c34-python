
name = "Monty"
age = 42
time_spent = 42.5


def concatenation(name, age, decimal):
    """ Return the combination of a string, integer and float into one\
        statement.

        Args:
            name(str): Person's name.
            age(int): Person's age.
            decimal(float): The amount of time the person has been alive.
        Return:
            Person's name, age, and estimated amount of time spent on \
            earth.
    """
    return "%s is %i years old, and has been alive approximately %f years." % \
        (name, age, time_spent)

print(concatenation(name, age, time_spent))

user_input = raw_input(u"Enter your name:")


def say_hello(name):
    """ Return the person's name and greet them.

        Arg:
            name(str): Person's name.
        Return:
            A greeting specific to that person.
    """
    if name.lower() == "buster":
        print(u"Heeeeeey brother!")
    elif name.lower() == "gob":
        print(u"I'm the guy in a $600 banana suit!")
    elif name.lower() == "george":
        print(u"And that's why you always leave a note!")
    elif name.lower() == "monty":
        print(u"I'm not dead yet!!")
    else:
        print(u"%s? I don't recognize %s. But hello anyway!") % \
            (user_input, user_input)

say_hello(user_input)


user = raw_input("Give me a name or a number:")


def string_or_integer(phrase):
    """ Return whether the variable input is a string, or a number hiding \
        within a string"

        Arg:
            phrase(str): Variable to be examined.
        Return:
            A statement that is conditional on whether the variable \
            is a string or a number.
    """
    if phrase.isdigit() is True:
        print(u"Wait, this is a number, what am I supposed to do with this!?")
    elif phrase.isalpha() is True:
        print(u"Good afternoon!")

string_or_integer(user)
