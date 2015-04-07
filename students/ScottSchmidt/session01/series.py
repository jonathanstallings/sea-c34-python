def fib(fibIndex):
    """ Return the nth number of the Fibonacci sequence.

        Arg:
            fibIndex: Provide Integer value argument for nth index of
            Fibonacci series.

        Return:
            Return single integer value of Fibonacci sequence at index,
            determined by function argument. """
    first, second = 0, 1
    for num in range(fibIndex):
        first, second = second, first + second
    return first


def lucas(lucIndex):
    """ Return the nth number of the Lucas sequence.

        Arg:
            lucIndex: Provide Integer value argument for nth index of Lucas
            series.

        Return:
            Return single integer value of Lucas sequence at index,
            determined by function argument. """
    first, second = 2, 1
    for num in range(lucIndex):
        first, second = second, first + second
    return first


def sum_series(nth, first=0, second=1):
    """ Return the nth number of the Lucas sequence from user input.

        Arg:
            nth: Provide Integer value argument for nth index of Lucas
            series.

            first: Optional parameter argument, determine the beginning
            integer value of the series.

            second: Optional parameter argument, determine the second
            integer value of the series.


        Return:
            Return single integer value of the sequence at index,
            determined by user input, and use optional argument values
            for first and second index values of series. """
    for num in range(nth):
        first, second = second, first + second
    return first


if __name__ == "__main__":
    """Test output values for each given index argument."""
    assert fib(10) == 55
    assert fib(11) == 89
    assert fib(12) == 144

    assert lucas(10) == 123
    assert lucas(11) == 199
    assert lucas(12) == 322

    assert sum_series(10) == 55
    assert sum_series(11, 2, 5) == 555
    assert sum_series(12, 4, 3) == 788
