def problem1():
    """Create a dictionary containing “name”, “city”, and “cake”
    for “Chris” from “Seattle” who likes “Chocolate”.
    Display the dictionary.
    Delete the entry for “cake”.
    Display the dictionary.
    Display the dictionary keys.
    Display the dictionary values.
    Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    Display whether or not “Mango” is a value in the dictionary.
    """

    lab = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
    print(lab)
    del lab["cake"]
    print(lab)
    lab["fruit"] = "Mango"
    print(lab.keys())
    print(lab.values())
    key = lab.keys()
    print("cake" in key)
    value = lab.values()
    print("Mango" in value)

problem1()



def problem2():
    """Using the dict constructor and zip, build a dictionary of numbers
    from zero to fifteen and the hexadecimal equivalent.
    """

    numbers = range(0, 16)
    result = dict(zip(numbers, [hex(hexadecimal) for hexadecimal in numbers]))
    print(result)

problem2()


def problem3():
    """Using the dictionary from item 1: Make a dictionary using the same
    keys but with the number of ‘a’s in each value.
    """

    new_lab = {}
    lab = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
    for a, number in lab.items():
        new_lab[a] = number.count("a")
        print(new_lab)

problem3()



def problem4():
    """Create sets s2, s3 and s4 that contain numbers from zero through twenty,
    divisible 2, 3 and 4.
    Display the sets.
    Display if s3 is a subset of s2 (False)
    and if s4 is a subset of s2 (True).
    """

    s2 = set(range(0, 21)[::2])
    s3 = set(range(0, 21)[::3])
    s4 = set(range(0, 21)[::4])
    print(s2)
    print(s3)
    print(s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))

problem4()




def problem5():
    """Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    Create a frozenset with the letters in ‘marathon’
    display the union and intersection of the two sets.
    """

    python = set("Python")
    python.add("i")
    marathon = frozenset("marathon")
    print(python.union(marathon))
    print(marathon.intersection(python))

problem5()





