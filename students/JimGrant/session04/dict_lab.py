#!/usr/bin/env python


def print_series_header(series_num):
    """Print a header for each dict lab series output, to aid in reading."""

    print(u"-------------------")
    print(u"Dict Lab - Series {}".format(series_num))
    print(u"-------------------")


def print_series_step(series_num, step_num, output):
    """Print the current state of the dict list series as a formatted string
    with the series number and step number.
    """

    print(u"{}.{} - {}".format(series_num, step_num, output))


def series1():
    print_series_header(1)
    d = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
    print_series_step(1, 1, "Current Dict: {}".format(d))
    d.pop("cake")
    print_series_step(1, 2, "Current Dict: {}".format(d))
    d["fruit"] = "Mango"
    print_series_step(1, 3, "Current Dict: {}".format(d))
    keys = d.keys()
    print_series_step(1, 4, "Keys: {}".format(keys))
    values = d.values()
    print_series_step(1, 5, "Values: {}".format(values))
    has_cake_key = "cake" in keys
    print_series_step(1, 6, "Has Cake Key: {}".format(has_cake_key))
    has_mango_val = "Mango" in values
    print_series_step(1, 7, "Has Mango Value: {}".format(has_mango_val))

    return d


def series2():
    print_series_header(2)
    r = range(0, 16)
    d = dict(zip(r, [hex(i) for i in r]))
    print_series_step(2, 1, "Int To Hex: {}".format(d))


def series3(s1_dict):
    print_series_header(3)
    d = {}
    for a, b in s1_dict.items():
        d[a] = b.count("a")
    print_series_step(3, 1, "Original Dict: {}".format(s1_dict))
    print_series_step(3, 2, "'a' Count of Dict Values: {}".format(d))


def series4():
    print_series_header(4)
    s2 = set(range(0, 21)[::2])
    s3 = set(range(0, 21)[::3])
    s4 = set(range(0, 21)[::4])
    print_series_step(4, 1, "s2: {}".format(s2))
    print_series_step(4, 2, "s3: {}".format(s3))
    print_series_step(4, 3, "s4: {}".format(s4))
    print_series_step(4, 4, "s3 is a subset of s2: {}".format(s3.issubset(s2)))
    print_series_step(4, 5, "s4 is a subset of s2: {}".format(s4.issubset(s2)))


def series5():
    print_series_header(5)
    s = set("Python")
    s.add("i")
    fs = frozenset("marathon")
    print_series_step(5, 1, "Union: {}".format(s.union(fs)))
    print_series_step(5, 2, "Intersection: {}".format(s.intersection(fs)))


if __name__ == "__main__":
    s1_dict = series1()
    series2()
    series3(s1_dict)
    series4()
    series5()
