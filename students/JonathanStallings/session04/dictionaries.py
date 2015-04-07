# 4 Questions
def test_wrong_key():
    """What happens when I try to access a a non-existing key?"""
    foo = {'bar': 15}
    print(foo['bar'])
    print(foo['barred'])


# test_wrong_key()
# result: Python raises a KeyError.


def dict_items_type():
    """What is the type of the output of .items() on a dictionary?"""
    foo = {'bar': 15, 'ziggy': 'zaggy'}
    print(type(foo.items()))


# dict_items_type()
# result: It is a list type!


def list_as_key():
    """What error occurs when trying list as key?"""
    foo = {[1, 2, 3]: 'bar'}
    print(foo)


# list_as_key()
# result: It throws a TypeError: unhashable type: 'list'.


def set_access_key():
    """What happens whey you try to access a set key?"""
    s = set([1, 2, 3])
    print(s)
    s[1]


# set_access_key()
# result: TypeError: 'set' object does not support indexing.
