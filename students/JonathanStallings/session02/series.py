def fibonacci(n):
    """Calculate the nth value of fibonacci series."""
    first, second = 0, 1
    if n == 0:
        value = first
    elif n == 1:
        value = second
    else:
        for x in range(2, n + 1):
            value = first + second
            first = second
            second = value
    return value


def lucas(n):
    """Calculate the nth value of lucas numbers series."""
    first, second = 2, 1
    if n == 0:
        value = first
    elif n == 1:
        value = second
    else:
        for x in range(2, n + 1):
            value = first + second
            first = second
            second = value
    return value


def sum_series(n, first=0, second=1):
    """Calculate the nth value of a sum series.

    Optional args:
        n: the number of the value to return.
        first: the first value of the series.
        second: the second value of the series.
    Returns:
        the nth value of the series.
    """
    if n == 0:
        value = first
    elif n == 1:
        value = second
    else:
        for x in range(2, n + 1):
            value = first + second
            first = second
            second = value
    return value


if __name__ == '__main__':
    # Check that the fibonacci and sum_series functions
    # give expected values.
    assert fibonacci(5) == 5 and sum_series(5) == 5
    # Check that the lucas and sum_series functions
    # give expected values.
    assert lucas(5) == 11 and sum_series(5, 2, 1) == 11
