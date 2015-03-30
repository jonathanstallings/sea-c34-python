# Dictionaries and Sets (4 questions)

# Question 1


def key_error():
    """
    What if I print ask to print a key that isn't in the dictionary?
    Result:
        KeyError: ('Maxwell')
        (line 19)
    """
    lob = {'Richard': 25, 'Earl': 29, 'Chancellor': 31, 'Williams': 26}
    print 'Legion of Boom:'
    print lob['Richard']
    print lob['Earl']
    print lob['Chancellor']
    print lob['Williams']
    print lob['Maxwell']

key_error()


# Question 2


def cant_add_to_dict():
    """
    What if I try to add a list as a key?
    Result:
        TypeError: unhashable type: 'list'
        (line 33)
    """
    seahawks = {}
    seahawks[(25, 29, 31, 26)] = 'LOB'
    seahawks[[3, 24, 88]] = 'Goal-Line Threats'

cant_add_to_dict()


# Question 3


def print_key_by_index():
    """
    What if I try to print a key by calling its print_key_by_index?
    Result:
        KeyError: (0,)
        (line 53) - You can't print a key by its index.
    """
    lob = {'Richard': 25, 'Earl': 29, 'Chancellor': 31, 'Williams': 26}
    print lob['Richard']
    print lob[0]

# Question 4


def add_to_frozenset():
    """
    What happens if I try adding to a frozenset?
    Result:
        AttributeError: 'frozenset' object has no attribute 'add'
        (line 53)

    """
    lob = frozenset(('Richard', 'Earl', 'Kam', 'Carey'))
    lob.add('Tebow')
