to_iterate = list(range(5))
print(to_iterate)


def iteration_counter(series):
    """ Return how many times the program iterates through a series of numbers.

        Arg:
            series(list): The list that will be iterated through to determine \
            the number of iterations.
        Return:
            The amount of times the program will iterate through the list of \
            numbers given.
    """
    number_of_iterations = []
    for number in series:
        number_of_iterations.append(number + 1)
    return len(range(number_of_iterations[-1]))

print iteration_counter(to_iterate)


my_phrase = "Hallo! My name is Inigo Montoya. You killed my father; prepare to \
die!"


def letter_count(phrase):
    """ Return how many "l"'s are within a given string

        Arg:
            phrase(str): The string that will be iterated through to \
            determine the number of "l"'s within it.
        Return:
            How many times "l" is used in a given sentence.
    """
    number_of_l = 0

    for i in phrase.lower():
        if i == "l":
            number_of_l += 1
    return str(number_of_l) + " 'l's are in this phrase."

print(letter_count(my_phrase))

num = list(range(138))


def odd_count(numbers):
    """Return the number of odd numbers from a list 0-137.

        Arg:
        numbers(lst):
            The series that will be itereated through to determine \
            the number of odd numbers within it.
        Return:
            How many odd numbers are in the list 0-137
    """
    odd = []

    for i in numbers:
        if i % 2 != 0:
            odd.append(i)
    return len(odd)

print(odd_count(num))
