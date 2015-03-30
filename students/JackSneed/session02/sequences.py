def compound_words():
    """Can compound words be generated from a list?"""

    some_compound = [u'some', u'thing', u'where', u'how', u'one']
    for i in range(1, len(some_compound)):
        first_word = some_compound[: -4]
        second_word = some_compound[i]

        print(first_word, second_word)

compound_words()
#Next would be to remove perenthesis, brackets, and commas from the results




def reduction():
    """Hypothetically, suppose there are too many Starbucks.

    This is determined because profits have dropped in all locations
    due to saturation. However profits have decreased evenly in all stores
    and other than flagships, overhead is the same.

    No one in corporate wants to take the full blame for the closures.

    Can we write a simple sequence function to determine which stores to close?
    """

    starbucks_per_city_gone = range(100)
    for i in starbucks_per_city_gone:
    # A step count of eleven should cut 17 out of 100
        del starbucks_per_city_gone[1:100:11]

    print(starbucks_per_city_gone)


reduction()




def find_that_word():
    """Can specific words be found in a one word string?"""

    hidden_word = u"jlijerfpojflmdewlmfoundmewepvakjmkf"
    if u"foundme" in hidden_word:
        print(u"Found that word!!")

find_that_word()
