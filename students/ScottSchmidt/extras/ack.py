def ack(m, n):
    """Return whole integer values when arguments passed into Ackermann
    function.
        arg:
            m: Integer value from 0 to 3 will return whole integers. Higher
            values will return exponential values.
            n: Integer value from 0 to 4 will return whole integers. Higher
            values will return exponential values.
        return: Will return produce whole integers given small argumental
        integers. Larger values have exponential increases, and when run
        will produce runtime recursion errors at command line. """

    if m < 0 or n < 0:
        return "Invalid argument, must be absolute integers."
    if m == 0:
        return n + 1
    elif m > 0:
        if n == 0:
            return ack(m-1, 1)
        elif n > 0:
            return ack(m-1, ack(m, n-1))

if __name__ == "__main__":
    if ack(2, 2) == 7:
        print "Test OK ack(2, 2)"
    if ack(3, 4) == 125:
        print "Test OK ack(3, 4)"
    if ack(-2, 3) is not int:
        print "Test OK ack(-2, 3)"
    if ack(0, 2) == 3:
        print "Test OK ack(0, 2)"
