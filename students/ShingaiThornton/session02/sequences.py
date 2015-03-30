#Question 1: Can two lists contain different object types can be concatenated?


def listAddition():
    """ 
    Concatenate two lists containing different object types
        Args: n/a

        Returns: n/a
    """
    x = [1,2, 3]
    y = ['b', 'a', 'y']
    z = x + y
    print z

listAddition()

#Q2: Can an index be concatenated with a slice?

def printString():
    """ 
    Concatenate the index and slice of a string and print results

        Args: n/a

        Returns: n/a

    """
    s = "This is a string of letters"
    print s[5] + s[1:5]

printString()


#Q3: What is Duck typing?

def duckTyping():

    """ 
    Create classes Cow and Person containing the methods moo and chew

        Args: n/a

        Returns: n/a

    """

    class Cow: 
        def moo(self):
            print "Mooooooo!"
        def chew(self):
            print"Chomp, chomp, chomp"
    class Person:
        def moo(self):
            print "I'm mooing!"
        def chew(self):
            print "I'm chewing!"

    def on_the_farm(animal):
        animal.moo()
        animal.chew()

    on_the_farm(Cow())
    on_the_farm(Person())

duckTyping()





