'''
This is for Task 12- Exploring Session 5- Comprehensions

The following functions were written to help clarify some
questions and misunderstandings I had while reviewing the
session 5 lecture notes. Each question will be noted by a
comment line #

Kimberlee Nighelli - 30 March 2015
'''

'''
To understand list comprehensions better, I'm
going to try to create a new list that takes in a number
from 0 to 20 and returns the number times 3 IF the number
is less than 10. I could just do range(11), but I wanted
to try to add a conditional!
'''

# Question 1: What does a for loop look like in list
# comprehension form?


def list_comp_for_loop():
    '''
    Creates a new list of x*3 for x <= 10
    '''
    new_list = [x * 3 for x in range(21) if x <= 10]
    return new_list


# Question 2: Can you use a list comprehension on a set
# to make a new set with only elements that are words?

def list_comp_sets(dirty_set):
    '''
    Goes through a set and creates a new set from the
    words that pass the .isalpha() function
    '''
    clean_set = {word for word in dirty_set if word.isalpha()}
    return clean_set

# Question 3: How does one use a dictionary comprehension?


def list_comp_dicts():
    '''
    Goes through a range and creates a new dictionary
    of the odd values
    '''
    odds = {i: "odd_number" for i in range(31) if i % 2 != 0}
    return odds

if __name__ == "__main__":

    print list_comp_for_loop()

    BAD_SET = ("Henry", "Potato", "164beacon", "57!!73", "Yay")
    print list_comp_sets(BAD_SET)

    print list_comp_dicts()
