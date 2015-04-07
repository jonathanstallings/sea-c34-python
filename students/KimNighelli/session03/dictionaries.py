'''
This is for Task 8 - Dictionaries
In this task, we were asked to come up with 4 questions that we had
while reading through the session 4 lecture notes. 
'''

# Question 1: How does one loop through all of the items in a dictionary? All of the values? Keys?

def dict_loops(some_dict):

    keys = []
    values = []

    print "The key-value pairs in the dictionary are (unsorted):" 
    
    for key, value in some_dict.items():
        print key, ":",  value
        
    # This is redundant, but I wanted to practice    
    for key in some_dict.keys():
        keys.append(key)
    for value in some_dict.values():
        values.append(value)
      
    print "\nTo reiterate, the keys are %s and the values are %s\n\n" % (keys, values)

# Question 2: Can you edit the value of a key value pair in a dictionary?
# Say you're going on a work trip. While making your packing list, you boss
# calls and says you need to extend the trip by 3 days. You'll need three more
# pairs of everything, except the laptop and cell phone charger.

def packing_list_add(some_dict):

    print "The original packing list was: ", some_dict

    for key, value in some_dict.items():
        if key != "Laptop" and key != "Cell Phone Charger":
            some_dict[key] = value + 3


    print "\nThe new packing list is ", some_dict
    return packing_list

# Question 3: How do you add an item to a dictionary?
# The boss lied. You also need to bring the pamplets because your co-worker forgot
# them. Update the packing list.

def update_list(some_dict):
    some_dict["Pamplets"] = 600
    print "\nNew packing list with forgotten pamphlets- ", some_dict


# Question 4: How to use zip
# You want to teach your child their square, and thought you'd try a different
# method. Instead of a table and writing everything, you'd print a list, just 
# in case they'd learn better from that. You also want to do this with zip, 
# because you just learned about it.
#
# NOTE: Yes, you can do this with regular math operations (ex: return x**2). But this helped me realize
# zip doesn't multiply the first item in list_x with all the items in list_y and so 
# on. It simply does what it needs with the current element of each list. 

def times_tables():
    x = y = range(21)
    print "\nThe squares for 0-20 are: "
    for x, y in zip(x, y):
        print "%d squared = %d" % (x, x*y) 


if __name__ == "__main__":


    test_dict = {
            "Country" : "United States",
            "State" : "Washington",
            "City" : "Seattle",
            "Street" : "Dexter Ave N",
            "House Number" : 801
            }

    dict_loops(test_dict)

    packing_list = {
            "Shirts" : 4,
            "Pants" : 3,
            "Socks" : 5,
            "Underwear" : 5,
            "Laptop" : 1, 
            "Cell Phone Charger" : 1
            }

    packing_list_add(packing_list)

    update_list(packing_list)

    times_tables()

'''
Output:
The key-value pairs in the dictionary are (unsorted):
    House Number : 801
    Country : United States
    State : Washington
    Street : Dexter Ave N
    City : Seattle

    To reiterate, the keys are ['House Number', 'Country', 'State', 'Street', 'City'] and the values are [801, 'United States', 'Washington', 'Dexter Ave N', 'Seattle']


    The original packing list was:  {'Underwear': 5, 'Laptop': 1, 'Cell Phone Charger': 1, 'Socks': 5, 'Shirts': 4, 'Pants': 3}

    The new packing list is  {'Underwear': 8, 'Laptop': 1, 'Cell Phone Charger': 1, 'Socks': 8, 'Shirts': 7, 'Pants': 6}

    New packing list with forgotten pamphlets-  {'Underwear': 8, 'Laptop': 1, 'Cell Phone Charger': 1, 'Socks': 8, 'Shirts': 7, 'Pamplets': 600, 'Pants': 6}

    The squares for 0-20 are:
    0 squared = 0
    1 squared = 1
    2 squared = 4
    3 squared = 9
    4 squared = 16
    5 squared = 25
    6 squared = 36
    7 squared = 49
    8 squared = 64
    9 squared = 81
    10 squared = 100
    11 squared = 121
    12 squared = 144
    13 squared = 169
    14 squared = 196
    15 squared = 225
    16 squared = 256
    17 squared = 289
    18 squared = 324
    19 squared = 361
    20 squared = 400
'''
