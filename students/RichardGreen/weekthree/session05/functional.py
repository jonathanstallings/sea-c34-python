'''Argument Functions
Richard Green
Foundations 2 Python'''

# Functional programming

x = range(0, 20)

# map


def funct_map(x):
    '''Question:Can I use functional programming to determine the ranges of
    a set of integers? Arguments: a range of integers'''

    return map(range, x)

# lambda


def funct_filter(x):
    '''Question:How can I use lambda to filter a data set to
    only look for those values not divisible by 2? Arguments: a string
    (range of integers)'''
    return filter(lambda x: x % 2, x)

# reduce


def funct_app_reduce(x):
    '''Question:How can I use lambda to reduce a data set to
    into a single value (get its sum)? Arguments: a string
    (range of integers)'''
    for i in range(0, 5):
        return reduce(lambda a, b: a + b, x)

if __name__ == "__main__":
    print funct_map(x)

    print funct_filter(x)

    print funct_app_reduce(x)
