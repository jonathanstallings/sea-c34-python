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
    

if __name__ == '__main__':
    section01()
    section02()
    section03()

