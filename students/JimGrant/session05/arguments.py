def question01():
    """Can I break the reference if I make a shallow copy inside a list of
    lists?
    """
    print("1. Can I break the reference if I make a shallow copy inside a list"
          "of lists?")
    orig_list = [[1, 2, 3], ["a", "b", "c"]]
    copy_list = orig_list[:]
    print("Orig List: {}".format(orig_list))
    print("Copy List: {}".format(copy_list))

    orig_list[0].append(4)
    print("Orig List: {}".format(orig_list))
    print("Copy List: {}".format(copy_list))

    orig_list[1] = orig_list[1][:]
    orig_list[1].append('d')
    print("Orig List: {}".format(orig_list))
    print("Copy List: {}".format(copy_list))
    print("Answer: Yes")


def question02():
    """Can I use list() as a default arg to generate a new list each time?"""
    print("Can I use list() as a default arg to make a new list each time?")

    def list_fun(x, l=list()):
        l.append(x)
        print(l)

    list_fun(3)
    list_fun(4)
    print("Answer: No")


def question03():
    """Can I use * to have a changeable number of arguments?"""
    print("Can I use * to have a changeable number of arguments?")

    def so_many_args(*args):
        for a in args:
            print(a)

    so_many_args("lambs", "sloths", "carp", "anchovies", "orangutangs",
                 "breakfast cereals", "fruit bats", "large chu...")
    print("Answer: Yes")


if __name__ == "__main__":
    question01()
    print("")
    question02()
    print("")
    question03()