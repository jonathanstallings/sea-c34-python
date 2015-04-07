
def fibonacci(n=5):
    '''This function performs a fibonacci series based off of a single user
    defined value.The function should returns  ``nth`` value in the fibonacci
    series
    Numeric arguments:
    n an integer
    Returns: an integer
    '''
    # Returns the fibonacci series based off a user defined number
    if n == 0:
            return 0
    elif n == 1:
            return 1
    else:
            return fibonacci(n - 1) + fibonacci(n - 2)

# lucas numbers function


def lucas(n):
    '''This function performs a lucas number series using an integer
    defined value. This function is similar to a fibonacci but instead of
    starting with integers 0 and 1 its starts with 2 and 1. The function
    should return  the ``nth`` value in the lucas number series.
    Numeric arguments:
    n an integer
    Returns: an integer
    '''
    # Returns the lucas numbers based off a user defined number
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, first=0, second=1):

    '''This function performs a sum series based off the previous functions
    outlined above: the fibonacci and lucas numbers and is based off a single
    user defined value and 2 optional user defined values. This function has
    default values of 0 and 1 to determine the first two values in the series
    to be produced. With no optional paramters the function produces numbers
    from the fibonacci series function. With optional arguments 2 and 1 the
    function produces the lucas numbers series. When other values for the
    optional parameters are entered the function will produce a different nth
    value in its series.
    Numeric arguments:
    n an integer
    first an integer
    second an integer
    Returns: an integer
    '''

    if first == 0 and second == 0:
        return fibonacci(n)
    if first == 2 and second == 1:
        return lucas(n)
    if n == first:
        return first
    elif n == second:
        return second
    else:
        return sum_series(n - first + sum_series(n - second))

if __name__ == "__main__":
    # lets test the fibnonacci module on an increasing set of integers
    print(fibonacci(1))
    print(fibonacci(5))
    print(fibonacci(7))
    print(fibonacci(15))
    # now lets test the lucas numbers function on a set of integers
    print(lucas(7))
    print(lucas(10))
    print(lucas(15))
    # And lastly we test our sum series function
    # on an increasing set of integers
    print(sum_series(range(4), first=1, second=5))
    print(sum_series(2))
    #print(sum_series(3, first=2, second=1))
