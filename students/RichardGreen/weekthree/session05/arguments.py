'''Argument Functions
Richard Green
Foundations 2 Python'''

# Advanced Argument Passing


def f0(x, y=0, z=2):
    '''Question what is the sum and product of the following
    integers? Description: This function accepts two numbers to add and
    multiples its sum. It emphaszies the use of argument passing.
    This will run with or without a z argument because a default
    has been provided Arguments: 3 integers. 2 mandatory the third
    optional'''
    print(x + y * z)


def f1(x, y, z=0, t=12):
    '''Question: using functional arguments can we capture the x,y,
    z(optional) axises and time(optional)? Description: This function
    captures different dimensional values. x, y, z and the fourth is
    time (hour). All are integers. Some data will only have x and y
    so they mandatory. This function highlights the optional arguments
    and functional arguments in variables. Arguments: 2 mandatory and
    2 optional '''
    results = u"xy_positions: %i, %i -- z_time: %i, %i"
    print(results % (x, y, z, t))


def f2(*args, **kwargs):
    '''Question: Can you capture the content that utilizes and distiguishes
    between the positional and optional content and can accept a range of
    values? Description: capture Arguments: mandatory and optional strings'''
    print(u"positional arguments are: %s" % unicode(args))
    print(u"optional arguments are: %s" % unicode(kwargs))

if __name__ == "__main__":

    f0(5, y=3, z=2)
    f0(1, y=2)

    f1(1, 7, z=15, t=23)
    f1(2, 3)
    # This function is using functional arguments in the form of:
    # a tuple (positional arguments)
    # a dict (keyword arguments)

    xy_position = (3, 4)
    z_time = {'z': 250, 't': 7}

    f1(*xy_position, **z_time)
    # Passing positional and optional arguments into the function

    f2(2, 3, age=5, year_born=5)
    # Lets run without the optional arguments
    f2(15, 17)
    f2(15, 17, 50, 75)
