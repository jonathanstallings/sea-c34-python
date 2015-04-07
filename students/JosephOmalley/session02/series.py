"""Joseph O'Malley"""
"""Fibonacci function"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

"""Lucas function"""
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

"""Optional starting values function (sum_series)"""
def sum_series(n, x=0, y=1):
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)

"""Test assertions on functions"""
if __name__ == "__main__":
    assert fibonacci(6) == 8
    assert lucas(6) == 18
    assert sum_series(5, 6, 4) == 38








