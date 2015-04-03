food_prefs = {
    u"name": u"Jonathan",
    u"city": u"Seattle",
    u"cake": u"chocolate",
    u"fruit": u"plum",
    u"salad": u"ceasar",
    u"pasta": u"lasagna"
}


def section01():
    """Complete the task for Section 1."""
    print(
        "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, "
        "{salad} salad, and {pasta} pasta."
        .format(**food_prefs)
    )


def section02():
    """Complete the task for Section 2."""
    key_num = range(16)
    val_hex = [hex(v) for v in key_num]
    the_dict = dict([(k, v) for k, v in zip(key_num, val_hex)])
    print(the_dict)


def section03():
    """Complete the task for Section 3."""
    the_dict = {k: hex(k) for k in range(16)}
    print(the_dict)


def section04():
    """Complete the task for Section 4."""
    the_dict = {k: v.count('a') for k, v in food_prefs.items()}
    print(the_dict)


def section05():
    """Complete the tasks for Section 5."""
    # Part a
    s2 = {x for x in range(21) if (x % 2 == 0)}
    s3 = {x for x in range(21) if (x % 3 == 0)}
    s4 = {x for x in range(21) if (x % 4 == 0)}
    print(s2)
    print(s3)
    print(s4)

    # Part b
    sets = s2, s3, s4 = (set(), set(), set())
    for i, set_x in zip((2, 3, 4), sets):
        for j in range(21):
            if j % i == 0:
                set_x.add(j)
    print(s2)
    print(s3)
    print(s4)

    # Part c
    s2, s3, s4 = [{x for x in range(21) if x % y == 0} for y in range(2, 5)]
    print(s2)
    print(s3)
    print(s4)


if __name__ == '__main__':
    section01()
    section02()
    section03()
    section04()
    section05()

