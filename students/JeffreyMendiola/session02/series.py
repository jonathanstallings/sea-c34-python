# Fibonacci Series
# 0, 1, 1, 2, 3, 5, 8, 13, ...

def fibonacci(n):
    """
    Return the nth value in the fibonacci series, starting at 0

    Args:
        n: the desired index to find in the fibonacci series.
    Returns:
        the value of the desired index in the fibonacci series.
    """
    b1 = 0
    b2 = 1
    if n > 1:
        counter = 3
        while (counter <= n):
            b3 = b1 + b2
            b1 = b2
            b2 = b3
            counter += 1
        b3 = b1 + b2
    elif n > 0:
        b3 = b2
    else:
        b3 = b1
    return b3


# Lucas Numbers
# 2, 1, 3, 4, 7, 11, 18, 29, ...

def lucas(n):
    """
    Return the nth value in the lucas series.

    Args:
        n: the desired index to find in the lucas series.
    Returns:
        the value of the desired index in the lucas series.
    """
    b1 = 2
    b2 = 1
    if n > 1:
        counter = 3
        while (counter <= n):
            b3 = b1 + b2
            b1 = b2
            b2 = b3
            counter += 1
        b3 = b1 + b2
    elif n > 0:
        b3 = b2
    else:
        b3 = b1
    return b3


# Sum Series

def sum_series(x, y=0, z=1):
    """
    Return the nth value in the sum series.

    Args:
        x: the desired index to find in the sum series.
        y: optional argument to change the 1st default value.
        z: optional argument to change the 2nd default value.
    Returns:
        the value of the desired index in the sum series.
    """
    b1 = y
    b2 = z
    if x > 1:
        counter = 3
        while (counter <= x):
            b3 = b1 + b2
            b1 = b2
            b2 = b3
            counter += 1
        b3 = b1 + b2
    elif x > 0:
        b3 = b2
    else:
        b3 = b1
    return b3
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# 2, 1, 3, 4, 7, 11, 18, 29, ...
if __name__ == "__main__":
    # fibonacci tests
    assert(fibonacci(0) == 0)
    assert(fibonacci(1) == 1)
    assert(fibonacci(2) == 1)
    assert(fibonacci(3) == 2)
    assert(fibonacci(4) == 3)
    assert(fibonacci(5) == 5)
    assert(fibonacci(6) == 8)
    assert(fibonacci(7) == 13)

    # lucas numbers tests
    assert(lucas(0) == 2)
    assert(lucas(1) == 1)
    assert(lucas(2) == 3)
    assert(lucas(3) == 4)
    assert(lucas(4) == 7)
    assert(lucas(5) == 11)
    assert(lucas(6) == 18)
    assert(lucas(7) == 29)

    # sum series tests
    assert(sum_series(0, 10, 20) == 10)
    assert(sum_series(1, 10, 20) == 20)
    assert(sum_series(2, 10, 20) == 30)
    assert(sum_series(3, 10, 20) == 50)
    assert(sum_series(4, 10, 20) == 80)
    assert(sum_series(5, 10, 20) == 130)
    assert(sum_series(6, 10, 20) == 210)
    assert(sum_series(7, 10, 20) == 340)
