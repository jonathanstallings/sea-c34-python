new_dictionary = {"name": "Bob", "age": "43", "weight": "150"}
name_list = ["Thomas", "Richard", "Harold"]


def add_list(n):
    """ Can a list be held within a dictionary as a value?

        Arg:
            n(lst): A list that will be added to the dictionary.
        Return:
            Return and print a dictionary that contains a list.
    """
    new_dictionary["name"] = n
    print(new_dictionary)

add_list(name_list)


def iterate_through_dict(example_dict):
    """ Iterate through a dictionary and return only a specific value.

        Arg:
            example_dict(dict): The dictionary to be iterated through.
        Return:
            Return the specific value we're looking for within the dictionary.
    """
    for k, v in example_dict.items():
        if v == "43":
            print("%s" % (v))

iterate_through_dict(new_dictionary)


my_set = set([1, 2, 3, 4, 5, 6])


def set_popper(n):
    """ Can a specific value be "popped" from a set?

    Arg:
        n(set): Set to have value popped from.
    Return:
        Return a singular popped value from the set.
    """
    print(n.pop())  # Error for popping specific value. Apparently not possible

set_popper(my_set)


def set_remover(n):
    """ Can multiple values be removed from a set at once?

    Arg:
        n(set): Set to have values removed from.
    Return:
        Return a set sans the removed values.
    """
    n.remove(6)  # Returns error remove() takes exactly 1 argument.
    # Will need further research to find alternate method.

set_remover(my_set)
print(my_set)
