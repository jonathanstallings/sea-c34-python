# Question: Will pytest be able to find and test this file, named per
# Task 18 directions?


def mult_2(x):
    """Return twice the input."""
    return x * 2


def test_mult_2_pass():
    """Test logic for mult_2."""
    assert mult_2(2) == 4


def test_mult_2_fail():
    """Test logic for mult_2."""
    assert mult_2(2) == 5


# result: Nope. Pytest finds files starting test_ or ending _test.

