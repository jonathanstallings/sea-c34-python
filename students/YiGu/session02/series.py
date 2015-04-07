# series.py module


def fibonacci(n):
    """This is Fibonacci fuction. The function return the nth value in the
     fibonacci series"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def lucas(n):
    """This is lucas fuction. The function return the nth value in the lucas
     series"""
    if n <= 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)


def sum_series(x, y=0, z=1):
    """sum_series has three parameteres x,y,z. x is the required parameter
will determine which element in the series to print.
y and z are the optional parameters will have default values of 0 and 1
and will determine the first two values for the series to be produced.
Calling this function with no optional parameters will produce numbers
from the fibonacci series. Calling it with the optional arguments 2 and
1 will produce values from the lucas numbers. Other values for the
optional parameters will produce other series."""
    if x < 0:
        print "series should not be less than 0"
        return None
    elif y == 2 and z == 1:
        return lucas(x)
    else:
        return fibonacci_sum_series(x, y, z)


def fibonacci_sum_series(x, y, z):
    """This is fibonacci_for_sum_series fuction. The function return the nth
value in the fibonacci series but user can change 0th & 1st fibonacci series
value"""
    if x == 0:
        return y
    elif x == 1:
        return z
    else:
        return fibonacci_sum_series(x-1, y, z)+fibonacci_sum_series(x-2, y, z)

# Main
if __name__ == "__main__":
    # assert statment
    # fibonacci
    assert fibonacci(0) == 0
    assert fibonacci(5) == 5
    assert sum_series(0) == 0
    # fibonacci
    assert sum_series(1) == 1
    assert sum_series(5) == 5
    assert sum_series(6) == 8
    assert sum_series(0, 2, 1) == 2
    # lucas
    assert sum_series(5, 2, 1) == 11
    assert sum_series(5, 3, 4) == 29
