food_prefs = {
    u"name": u"Jonathan",
    u"city": u"Seattle",
    u"cake": u"chocolate",
    u"fruit": u"plum",
    u"salad": u"ceasar",
    u"pasta": u"lasagna"
}


def section01():
    """Complete the task for seciton 1."""
    print(
        "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, "
        "{salad} salad, and {pasta} pasta."
        .format(**food_prefs)
    )


if __name__ == '__main__':
    section01()
