#Question: What happens when you copy a list and alter its copy?
def question_one(test_list, values):
    """
    Returns a list  to verify the changes on mutable features

    Args:
        test_list (list) : a list to be copied
        values (list) : values to be added to the list
    Returns:
        a list and its copy in a list. 
    """
    test_list = ["happy", "sad"]
    copy_list = test_list
    for value in values:
        copy_list.append(value)

    return [test_list, copy_list]

#Question 2: How can you insert a value in a tuple?
def question_two(test_tuple, index, feature):
    """
    Returns a tuple that has an element inserted at a given index

    Args:
        test_tupletuple (tuple) :  the tuple to be operated upon
        feature (unknown) : a value to be insterted into a tuple
        index (int) : the value at which the value should be inserted
    Returns:
        a tuple that is a copy of the argument tuple but with the addition 
        of an inserted value at an index. 

    """
    copied_tuple_list = []
    for value in test_tuple:
        copied_tuple_list.append(value)

    copied_tuple_list.insert(index, feature)

    return (tuple(copied_tuple_list))

# Question 3: Is list homgeneity enforced?
def question_three():
    """Returns a list that has multiple different types in it"""
    return ["cow", 1]

# ******************* TEST CODE ************************ #
if __name__ == '__main__':
    print("Testing Question One: What happens when you copy a list and\
    alter its copy?")
    print(question_one(["happy", "sad"], ["mad", "glad"]))
    print("Testing Question Two: How can you insert a value in a tuple?")
    print(question_two(("cows", "are", 4, "me"), 3, "test insertion"))
    print ("Testing Question Three: Is list homgeneity enforced?")
    print(question_three())
