""" 
Exploring Exception Types by intentionally including incorrect code
    
Thanks to the respondents in this stackoverflow thread for helping with the eval function:
http://stackoverflow.com/questions/25049498/failed-to-catch-syntax-error-python
"""


def Test_SyntaxError():
    try:
        eval('test = 1 + ')
    except SyntaxError:
        print("This function caused a Syntax Error")


def Test_TypeError():
    try:
        test = 1 + "cow"
    except TypeError:
        print("This function caused a Type Error")


def Test_NameError():
    try:
        test = cow
    except NameError:
        print("This function caused a Name Error")


def Test_AttributeError():
    try:
        test = "cow".test
    except AttributeError:
        print("This function caused a Attribute Error")


########## Tests ##########
if __name__ == "__main__":
    Test_NameError()
    Test_TypeError()
    Test_SyntaxError()
    Test_AttributeError()
    print("Tests Complete")
