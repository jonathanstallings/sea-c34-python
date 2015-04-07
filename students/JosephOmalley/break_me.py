def nameError(x):
    dog = x
    return cat

nameError(1)

def typeError(x, y):
    return x + y

typeError(1, "cat")

def syntaxError(x, y):
    return x + :)

sytaxError(1, 2)

def attributeError(x, y):
    return y.cat + x.cat

attributeError(1,2)