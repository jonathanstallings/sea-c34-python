import series as s


def test_fibonacci():
    assert s.fibonacci(5) == 5
    assert s.fibonacci(10) == 55


def test_lucas():
    assert s.lucas(5) == 11
    assert s.lucas(10) == 123


def test_sum_series():
    assert s.fibonacci(5) == s.sum_series(5)
    assert s.lucas(5) == s.sum_series(5, 2, 1)

