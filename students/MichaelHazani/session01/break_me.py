# The Manny Errors in Python

# Or at least some common ones:


# Syntax Error:
function syntaxErr():


# Name Error:
def nameErr():
    2 + cat


# Type Error:
def typeErr():
    2 + "cat"


# Attribute Error:
def attErr():
    numList = [0, 1, 2, 3]
    print(numList.cat)
