
#Q1: Can the .format() method be used on the same line as place holders?

def placeHolding():
    """
        Print string using place holders and .format()method
            Args: 
            Returns:

    """
    print "Hi, {}, how's your {} ?  And your %s ?".format("Bob", "wife") %('kids')

placeHolding()

#Q2: Can the raw_input function accept a list as input?

def listInput():
    """
        Ask the user to enter a list
            Args: n/a
            Returns: n/a
    """
    list = raw_input('Please enter a list')
    print list

listInput()


#Q3: Will calling .upper() .lower() and .title() on numeric types produce an error?

def numberOperations():
    """
        Call the .upper, .lower, and .title functions on the number 42
        Args:
        Returns:
    """
    x = 42
    x.upper()
    x.lower()
    x.title()
numberOperations()