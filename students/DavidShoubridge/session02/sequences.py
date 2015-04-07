def slice_it_up(sequence):
    """
    Return what are the first 5 values from a list beginning at 45 and ending \
    at 57.

    Arg:
        sequence(lst): List that will be sliced.
    Return:
        The the values of a slice of a sequence from 0 to 5.

    """
    return sequence[0:5]


print(slice_it_up(range(45, 57)))

my_string = "This is a string whose length will now be determined."


def string_length(string):
    """
    Return what is the length of the phrase: 'This is a string whose length \
    will now be determined.'

    Arg:
        string(str): String whose length will be counted.
    Return:
        The length of given string.
    """
    return "The string is " + str(len(string)) + " characters long."

print(string_length(my_string))


def contain_zebra(string):
    """ Return whether the phrase stored in my_string contains the word \
    'zebra'.

    Arg:
        string(str): String that will be examined for given phrase.
    Return:
        Whether it's true or false that the string contains the word 'zebra'
    """
    return "zebra" in string

print(contain_zebra(my_string))
