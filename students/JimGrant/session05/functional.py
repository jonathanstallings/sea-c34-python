def question01():
    """Can I use a lambda in a list comprehension?"""
    print("Can I use a lambda in a list comprehension?")
    l = lambda x, y: x + y
    ls = [l(m, n) for m in range(0, 10) for n in range(0, 2)]
    print(ls)
    print("Answer: Yes")


def question02():
    """Will map() return a set if I feed it a set?"""
    print("Will map() return a set if I feed it a set?")
    s = {1, 2, 3}
    m = map(None, s)
    print(m)
    print("Answer: No")


def question03():
    """Can I use reduce() with strings?"""
    print("Can I use reduce() with strings?")
    s = ["a", "series", "of", "words"]
    r = reduce(lambda x, y: x + y, s)
    print(r)
    print("Answer: Yes")


if __name__ == "__main__":
    question01()
    print("")
    question02()
    print("")
    question03()