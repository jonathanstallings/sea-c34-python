"""
Have not been able to make the exceptions occur for second file_opener()
"""


def string_error():
    """ What happens if I try to divide a string?

    Arg(n): User Input.
    Return: An error.
    """
    user_input = raw_input("Enter a number")
    try:
        user_input / 2
    except TypeError:
        print("Input must be a string, sorreeeeeee")

string_error()


def file_opener():
    """ Can I write an exeption statement that works? I don't understand how \
    to use them yet.
    """
    try:
        open("gone.txt", "wb")
    except IOError:
        print("Couldn't open gone.text")

file_opener()
