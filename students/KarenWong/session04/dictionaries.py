def my_dict():
    """ Is it possible to add a key in an existing dictionary """
    my_list = {"name": "Karen", "horosope": "Germini"}
    my_list["zodiac"] = "sheep"
    print my_list


def unpack_dictionaries():
    """How to provide arguments to functions with the keys and values
    in the dictionary"""
    my_info = {"name": "Karen", "state": "washington"}
    print "Hi, my name is {name}! I live in {state}!".format(**my_info)


def loop_keys():
    """How to loop over keys in the dictionary?"""
    my_info = {"name": "Karen", "state": "washington"}
    for thing in my_info:
        print (thing)


def get_value():
    """How to get the values in the dictionary?"""
    my_info = {"name": "Karen", "state": "washington"}
    for value in my_info.values():
        print(value)
