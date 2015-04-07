def fib(n):
    """Return the nth value in the fibonacci series, starting at 0.""" 
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        return fib(n-1) + fib(n-2)
'''
print fib(0)
print fib(1)
print fib(2)
print fib(3)
print fib(5)
'''



def lucas(n):
    """Return the nth value in the Lucas Series, starting at 0."""
    if n == 0:
        return 2
    elif n == 1:
        return n
    else:
        return lucas(n-1) + lucas(n-2)

'''
print lucas(0)
print lucas(1)
print lucas(2)
print lucas(3)
print lucas(4)
'''



def sum_series(n, first_value=0, second_value=1):
    """Return the nth number in a recursive integer series.
    Args:
        n = positive integer; position from which series will return.
        first_value = int (0 by default, optional)
        second_value = int (1 by default, optional)
    """
    for i in range(n):
        first_value, second_value = second_value, first_value + second_value
    return first_value

'''
print sum_series(0)
print sum_series(1)
print sum_series(2)
print sum_series(3)
print sum_series(4)
print sum_series(5)
print sum_series(6)
print sum_series(7)
'''


if __name__ == "__main__":

# Test the fibonacci function    
    assert(fib(0) == 0)
    assert(fib(7) == 13)

# Test the lucas series function
    assert(lucas(0) == 2)
    assert(lucas(1) == 1)
    assert(lucas(7) == 29)

# Test sum_series with default values

    assert (sum_series(7) == 13)
# Test sum_series with custom values
    assert (sum_series(7, 2, 1) == 29)
    assert (sum_series(7, 3, 4) == 76)


print "Passed eight assertion statements"


