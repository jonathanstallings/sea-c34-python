def lambdacall():
    """can a lambda operation call another function?"""
    def add(x, y):
        return x + y

#     1 = [lambda x, y: x * y + add(x, y)]
    return 1[0](1, 2)

# print lambdacall()
# result: NO! "SyntaxError: can't assign to literal". Makes sense.


l = [2, 5, 7, 12, 6, 4]


def fun(x):
    """can you map a map? This is the first mapping function"""
    return x * 2


def morefun(x):
    """this is the second mapping function"""
    return x * 3

# print(map(fun, map(morefun, l)))
# result: absolutely! [12, 30, 42, 72, 36, 24]


def filterall():
    """can you filter based on conditions that aren't math?"""
    l = [1, 2, 3, 4, "val", 6, "val2", 8, 9, 0]
    print(filter(lambda x: type(x) is not int, l))
# filterall()
# result: absolutely! returns "['val', 'val2']"
