def NameError():
    return a+b

def TypeError():
   return 3+"2"

def SyntaxError():
    n=0
#    return n++

def AttributeError():
    n=0
    return n.append(3)

if __name__ == '__main__':
#    NameError()
#    TypeError()
#    SyntaxError()
    AttributeError()
