def fibonacci(n):
    """
    Return the nth value in the fibonacci series.
    Args:
        n: the value in the series to be returned.
    Returns:
        the nth value in the series.
    """
    num_series = [0, 1]
    for i in range(n+1):
        if i < 2:
            i = i+1
        else:
            num_series.append(num_series[i-1]+num_series[i-2])
            i = i+1
    return num_series[n-1]


def lucas(n):
    """
    Return the nth value in the lucas series.
    Args:
        n: the value in the series to be returned.
    Returns:
        the nth value in the series.
    """
    num_series = [2, 1]
    for i in range(n+1):
        if i < 2:
            i = i+1
        else:
            num_series.append(num_series[i-1]+num_series[i-2])
            i = i+1
    return num_series[n-1]


def sum_series(n, val1=0, val2=1):
    """
    Return the nth value in either the fibonacci or lucas series.
    The default result will be the fibonacci series.
    Args:
        n: the value in the series to be returned.
        val1 (optional): the first value in the series.
        val2 (optional): the second value in the series.
    Returns:
        the nth value in the series.
        val1=0, val2=1 will give the fibonacci series.
        val1=2, val2=1 will give the lucas series.
        other values will give "some other series".
    """
    if val1 == 0 and val2 == 1:
        return fibonacci(n)
    elif val1 == 2 and val2 == 1:
        return lucas(n)
    else:
        return "some other series"

if __name__ == "__main__":
    # add assert statement to test performance with specific values
    assert(sum_series(11, 0, 1)) == 55
    # this is the 11th value in the fibonacci series
    assert(sum_series(9, 2, 1)) == 47
    # this is the 9th value in the lucas series
    assert(sum_series(9, 7, 3)) == "some other series"
    # code seems to be performing as expected
    # I am not getting any assertion errors
