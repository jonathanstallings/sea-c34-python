def fibonacci(n):
    """
    Calculate the fibonacci number of a given position, less than 100.

    Args:
        n: the position to get the nth fibonacci number of.
    Returns:
        the number in the nth position.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n - 1)) + (fibonacci(n - 2))

print fibonacci(0)
print fibonacci(1)
print fibonacci(4)
# print fibonacci(100) this hangs the computer up, though I can't tell if it's
# an infinite loop or if the computer will calculate eventually.


def lucas(n):
    """
    Calculate the lucas value of a given position.
    """
    num1 = 2
    num2 = 1
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        while n > 1:
            num1 += lucas(n - num1)
            num2 += lucas(n - num2)
            return num1 + num2

print lucas(2)
print lucas(4)
