#Each function should result in one of the four common exceptions from
#our lecture. for review: NameError, TypeError, SyntaxError, AttributeError


def breakname(number):
    newnumber = number + 1
    return newbienumber

breakname(4)  #name error


def breaksyntax(name):
    '''
    say hello given a name
    '''
    return "Hello, " + a

breaksyntax(Mary)  #syntax error


def breaktype(a):
    return a

breaktype(2, 4)  #type error


def breakattribute():
    class MyClass:
        """A simple example class"""
        i = 12345
        def f(self):
            return 'hello world'
    print MyClass.j

breakattribute()  #attribute error
