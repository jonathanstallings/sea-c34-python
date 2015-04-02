def build_donors_dict ():
    """ Would it be possible to use a dictionary for the task7 Mail Room Madness"""
    donors = {}
    donors["Le Chat"] = [1000, 200, 345]
    donors["El Perro"]= [2000000, 10, 10]
    donors["Bob"]= [15, 15, 15]

    for k, v in donors.items():
        print ("%s has donated: " % k)
        for donation in v:
            print ("%d " % donation)

    return donors

def dictionary_destruction (dict):
    """
    Something in the lecture notes made me think that iteration destroyed a 
    dictionary. To answer that question I will be using the dictionary created
    in the first function. Since it has already been iterated over, simply 
    displaying the dictionary passed in as a parameter should be suffcient
    to test this.  

    """
    print (dict)

def why_set ():
    """ What are some usecases for a set?"""
    #A set could be used to validate a response
    available_answers = set(["Send a Thank You", 'Create a Report'])
    answer = raw_input("Please select an option 'Send a Thank You' or 'Create a Report':")

    while answer not in available_answers:
        answer = raw_input("That is not a vaild answer. Please try again: ")

    print ("Ok lets %s." %answer)
    
def set_pop ():
    """
     Does set.pop only remove a random element? or can you specify which
     value can be popped
    """
    test_set = set(['happy', 'sad', 'mad'])
    try:
        print(test_set.pop("happy"))
    except TypeError:   
        print ("set.pop() doesn't take an arugment")
        print (test_set.pop())

#*********************** TEST CODE ***************************#
if __name__ == '__main__':
    print ("Investigating question one: ")
    this_dict = build_donors_dict()
    print ("Investigating question two: ")
    dictionary_destruction(this_dict)
    print ("Investigating question three: ")
    why_set()
    print ("Investigating question four: ")
    set_pop()