def reduction():
    odd_numbers = range(16)
    for x in odd_numbers:
        del odd_numbers[2:16:2]

    print(odd_numbers)

reduction()