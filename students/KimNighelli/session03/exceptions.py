'''
This is for Task 8 - Exceptions

Below, I ask two questions relating to exceptions that came up while
reading through the session04 lecture notes:

1) While in a loop, how to I bypass an element of a list that cannot have
a particular operation performed on it?

2) Given a dictionary, what happens if you try to call a key that doesn't exist?
'''

# Question 1: While in a loop, how to I bypass an element of a list that cannot have
# a particular operation performed on it?

def error_try(test_list):

    empty_list = []
    print "My test list is %s" % (test_list)

    for element in test_list:
        try:
            empty_list.append(element.upper())
        except AttributeError:
            print "Cannot perform .upper() on %s due to an Attribute Error" % (element)

    return empty_list

# Question 2: What exception arises if you try to call a key at an index that doesn't
# exist in a dictionary?

def bypass_keyindex(some_dict):
    
    common_keys = ["Name", "Address", "Age", "Occupation", "Favorite Food"]
    # Key
    for i in common_keys:
        try:
            print "They value associated with the key %s is %s" % (i.lower(), some_dict[i])
        except KeyError:
            print "A key of %s does not exist in this dictionary" %(i)


        

if __name__ == "__main__":
    
    # For Question 1

    test_list = ["Pen", 43, "Alligator", 89, "CoMiSsIoN", 76, 9, "Boston"]
    error_try(test_list)

    assert error_try(test_list) == ["PEN", "ALLIGATOR", "COMISSION", "BOSTON"]

    print("\n")
    
    # For Question 2

    test = {
            "Name" : "Kim",
            "Age" : 24,
            "Occupation" : "Meteorologist",
            "Favorite Food" : "Enchiladas"
            }

    bypass_keyindex(test)

    

'''
Output:
My test list is ['Pen', 43, 'Alligator', 89, 'CoMiSsIoN', 76, 9, 'Boston']
Cannot perform .upper() on 43 due to an Attribute Error
Cannot perform .upper() on 89 due to an Attribute Error
Cannot perform .upper() on 76 due to an Attribute Error
Cannot perform .upper() on 9 due to an Attribute Error


They value associated with the key name is Kim
A key of Address does not exist in this dictionary
They value associated with the key age is 24
They value associated with the key occupation is Meteorologist
They value associated with the key favorite food is Enchiladas
'''

