def egg_overload():
    """They say never put too many eggs in one basket.

    Can we write a function to do just that?
    """

    basket_capacity = 40
    eggs = 6

    while eggs <= basket_capacity:
        eggs += 6
        if eggs >= basket_capacity:
            print(u"The basket hath runneth over!")

egg_overload()




def roots():
    """Can iteration be used to find square roots?

    The goals is to find the square root of 5 using a
    bisection search.
    """

    low = 0
    high = 10
    sqrt = (high + low)/ 2.0

    # Use a small float to inrease accuracy
    while abs(sqrt**2 - 5) > 0.01:
        if sqrt**2 < 5:
            low = sqrt
        else:
            high = sqrt
        sqrt = (high + low)/ 2.0

        print(sqrt)

roots()




def something_simpler():
    """I wonder if I can double my list with each iteration in a function"""



    add_numbers = range(10)
    # The range should double my list with each iteration
    for i in range(3):
        add_numbers.extend(add_numbers)

    print(len(add_numbers))

something_simpler()
