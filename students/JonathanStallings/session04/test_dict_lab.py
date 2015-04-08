import dict_lab as dl


def test_divisible_set():
    s1 = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    assert dl.divisible_set(20, 2) == s1

