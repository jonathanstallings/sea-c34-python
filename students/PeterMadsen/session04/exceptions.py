def finally_vs_else():
    """ When might you use finally vs. else in an try block?"""

    print("Case 1 finally with a faliure in the try block")
    try:
        if 'cows' & 'cows':
            print ("Success!")
    except:
        print("This Failed")
    finally:
        print("This will happen no matter what goes on above!")

    print("Case 2 finally with a success in the try block")
    try:
        if 'cows' == 'cows':
            print ("Success!")
    except:
        print("This Failed")
    finally:
        print("This will happen no matter what goes on above!")

    print("Case 3: else with a faliure in the try block")
    try:
        if 'cows' & 'cows':
            print ("success!")
    except:
        print("This Failed")
    else:
        print("This will happen if no exception occurs!")

    print("Case 4: else with a success in the try block")
    try:
        if 'cows' == 'cows':
            print ("success!")
    except:
        print("This Failed")
    else:
        print("This will happen if no exception occurs!")

def using_except():
    """ Why is it better to not use a general except statment?"""

    user_input = 0

    print("You can provide bad feed back like this: ")
    try:
        print(12312/user_input)
    except:
        print ("That is not a valid answer: ")
    
    print ("You can provide good feedback like this: ")
    try:
        print(12312/user_input)
    except ZeroDivisionError:
        print ("You cannot divide by zero")
    except TypeError as this_error:
        print ("You cannot divide by that type: ", this_error)

#******************* Test Code **************************#
if __name__ == '__main__':
    print("Answering question one: ")
    finally_vs_else()
    print("Ansewering question two: ")
    using_except()