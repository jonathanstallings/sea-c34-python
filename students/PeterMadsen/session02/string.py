#Question 1: How many string conversion types are there?
def question_one():
    """Prints the answer to the stated question but not the why?"""
    print ("There are %d different conversion types according to Python Documentation" % 16)

#Question 2: Why do we have %i and %d for ints and %f and %F for floats?
def question_two(): 
    """Formats two different phrases using 4 different operators"""
    print ("Why are there %i ways to write an int" %2)
    print ("Why are there %d ways to write an int" %2)
    print ("Why are there %f ways to write a float" %2.0)
    print ("Why are there %F ways to write an float" %2.0)

#Question 3: Will the .format option take over all string operations?
def question_three():
    """This function Asks an essential Question"""
    print ('Will the {} method remain in use, or will'.format("classic")), 
    print('.... ("drum beats") the .%(method)s method take over the string formatting world?' % {u'method': u"format"})

# **************** TEST CODE ***************************#
if __name__ == '__main__':
    print("Question 1: How many string conversion types are there?")
    question_one()
    print ('#Question 2: Why do we have %i and %d for ints and %f and %F for floats?' )
    question_two()
    print ('#Question 3: Will the .format option take over all string operations?')
    question_three()