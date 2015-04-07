def question01():
    """Can I use zip in a comprehension to build a dict out of two lists?"""
    print("Can I use zip in a comprehension to build a dict out of two lists?")
    d = {a: b for a, b in zip(range(3), range(3, 6))}
    print(d)
    print("Answer: Yes")


def question02():
    """Can I use a string as a sequence for a comprehension?"""
    print("Can I use a string as a sequence for a comprehension?")
    l = [a for a in "aeiou"]
    print(l)
    print("Answer: Yes")


def question03():
    """Can I use a dict as a sequence for a comprehension?"""
    print("Can I use a dict as a sequence for a comprehension?")
    l = [a for a in {'a': 1, 'b': 2}]
    print(l)
    print("Answer: Yes, but it will give the keys, not the vals.")

if __name__ == "__main__":
    question01()
    print("")
    question02()
    print("")
    question03()