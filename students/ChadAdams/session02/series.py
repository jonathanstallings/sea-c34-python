def fibonacci(x):
    """
    Calculate Fibonacci sequence to the nth number.

    args:
        x: the nth number to display.
    returns:
        list containing Fibonacci sequence to the nth number.

    """
    a = 0
    b = 1
    c = 0
    fibo = [a]
    if x == 0:
        fibo = [a]
    elif x == 1:
        fibo = [a, b]
    else:
        fibo = [a, b]
        for i in range(x):
            c = a+b
            fibo.append(c)
            a = b
            b = c

    return fibo


def lucas(x):
    """
    Calculate Lucas sequence to the nth number.

    args:
        x: the nth number to display.
    returns:
        list containing Lucas sequence to the nth number.

    """
    a = 2
    b = 1
    c = 0
    lucas_list = [a]
    if x == 0:
        lucas_list = [a]
    elif x == 1:
        lucas_list = [a, b]
    else:
        lucas_list = [a, b]
        for i in range(x):
            c = a+b
            lucas_list.append(c)
            a = b
            b = c

    return lucas_list

def sum_series(x, a = 0, b = 1):
    """
    Calculates numberical sequence to the nth number based on the fibonacci
    algorithm.

    args:
        x: the nth number to display.
    returns:
        list containing numerical sequence to the nth number.

    """

    c = 0
    series_list = [a]
    if x == 0:
        series_list = [a]
    elif x == 1:
        series_list = [a, b]
    else:
        series_list = [a, b]
        for i in range(x):
            c = a+b
            series_list.append(c)
            a = b
            b = c

    return series_list

if __name__ == "__main__":
    #testing fibonacci function
    print fibonacci(0)
    print fibonacci(1)
    print fibonacci(6)
    print fibonacci(10)
    #testing lucas function
    print lucas(0)
    print lucas(1)
    print lucas(6)
    print lucas(10)
    #testing sum series with default fibonacci params
    print sum_series(0)
    print sum_series(1)
    print sum_series(6)
    print sum_series(10)
    #testing sum series with optional lucas params
    print sum_series(0,2,1)
    print sum_series(1,2,1)
    print sum_series(6,2,1)
    print sum_series(10,2,1)
    #testing sum series with optional random params
    print sum_series(10,4,6)
    print sum_series(10,1,2)
    print sum_series(10,0,0)
    print sum_series(10,3,11)
