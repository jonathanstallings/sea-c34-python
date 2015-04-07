def fibonacci(n):
    """
    Return the nth value in the Fibonacci Series.

    Arg:
        n(int): Element of the series whose value will print.
    Return:
        The value in the Fibonacci Series that corresponds to the value of n.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        series = [0, 1]
        for i in range(n - 1):
            series.append(series[i] + series[i + 1])
        return series[len(series) - 1]


def lucas(n):
    """
    Return the nth value in the Lucas Series.

    Arg:
        n(int): Element of the series whose value will print.
    Return:
        The value in the Lucas Series that corresponds to the value of n.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        series = [2, 1]
        for i in range(n - 1):
            series.append(series[i] + series[i + 1])
        return series[len(series) - 1]


def sum_series(n, x=0, y=1):
    """
    Return nth value from either Fibonacci Series or Lucas Series depending \
    on arguments. If only given (n), will return Fibonacci series. If given \
    (n, 2, 1) will return Lucas series. If given n with any other 2 numbers, \
    it will create it's own series and return the nth value.

    Args:
        n(int): Determines which element of the series whose value will print.
        x(int): Optional argument defaulted to 0, and will combine with y \
        to create series of integers.
        y(int): Optional argument defaulted to 1, and will combine with x \
        to create a series of integers.
    Return:
        The nth value in either the Fibonacci series, the Lucas series, \
        or another series based on the values given for x and y.
    """

    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        series = [x, y]
        for i in range(n - 1):
            series.append(series[i] + series[i + 1])
        return series[len(series) - 1]


if __name__ == "__main__":
    """
        The first 3 assert statements test whether the fibonacci function \
        will return the correct value that corresponds to the nth element \
        in the Fibonacci series.

        The second 3 assert statements test whether the lucas function \
        will return the correct value that corresponds to the nth element \
        in the Lucas series.

        The last 4 assert statements test whether the sum_series function, \
        given an argument n without any optional arguments, will return \
        the correct value from the Fibonacci series. Otherwise, it tests \
        whether given arguments n, x, and y the function will return \
        the correct value from either the Lucas series or, if x and y \
        are not 2, and 1, respectively, whether the function will return \
        the correct value from a series of numbers beginning with x and y \
        using the same logic as the Fibonacci and Lucas functions.
    """
    assert(fibonacci(1)) == 1
    assert(fibonacci(5)) == 5
    assert(fibonacci(7)) == 13

    assert(lucas(0)) == 2
    assert(lucas(3)) == 4
    assert(lucas(7)) == 29

    assert(sum_series(2)) == 1  # Testing for return from Fibonacci series.
    assert(sum_series(2, 2, 1)) == 3  # Testing for return from Lucas series.
    assert(sum_series(2, 4, 3)) == 7  # Testing for return from x and y series.
    assert(sum_series(6, 2, 1)) == 18  # Testing for return from Lucas series.
