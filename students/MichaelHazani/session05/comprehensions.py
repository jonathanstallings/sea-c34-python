def compremath():
    """can you do math in comprehensions?"""
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = [var * 8 for var in list1]
    return list2

# print compremath()
# result: yup! Returns [8, 16, 24, 32, 40, 48, 56, 64]


def comprevarimath():
    """can you utilize other variables in comprehensions?"""
#   list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#    list2 = [var - (var + 1) for var in list1]
#   return list2

# print comprevarimath()
# result: yes! Returns [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]


def comprewhile():
    """can you do a comprehension with a while loop?"""
    a = range(15)
    new_list = []
    (new_list.append(a) while a < 9)
    print new_list
comprewhile()
# result: doesn't seem like it!
