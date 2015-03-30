def another_variable():
    """Answers the following question.

    1. If I make a list variable and another variable that points at that list,
       can I modify the original list with that variable?
    """
    original = range(10)
    assert original[3] == 3
    another = original
    another[3] = 100
    assert original[3] == 100
    assert original[3] == another[3]
    original[5] = 12
    assert another[5] == 12
    another = range(10)
    another[3] = 200
    assert original[3] != another[3]


def sublist_shallowcopy():
    """

    2. If I copy a list and change one of the elements of the sublist, does it
        affect the elements of the sublist?
    """
    breakfast = ["sausage", "eggs", ["waffle", "blueberries"]]
    breakfast_copy = breakfast[:]
    breakfast_copy[0] = "bacon"
    breakfast_copy[2][1] = "strawberries"
    print (breakfast)
    print (breakfast_copy)


def sublist_deepcopy():
    """

    3. If I copy a list and change one of the elements of the sublist, is there
       a way that does not affect the elements of the sublist?
    """
    import copy
    breakfast = ["sausage", "eggs", ["waffle", "blueberries"]]
    breakfast_copy = copy.deepcopy(breakfast)
    breakfast_copy[2][1] = "strawberries"
    print (breakfast)
    print (breakfast_copy)
