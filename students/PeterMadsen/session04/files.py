import io 

def queston_one():
    """How would you draw a geometric feature in a  text file?"""
    try: 
        f = io.open('test.txt', 'w')
    except IOError:
        print ("That file doesn't exist at that location")

    space = 1
    for i in range(20):

        for j in range(space):
            f.write(u' ')
            j += 1
        f.write(u'x\n')
        space += 1
        if space > 20:
            break

def question_two():
    """What does the seek() method do?"""
    try: 
        f = io.open('test.txt', 'r')
    except IOError:
        print ("That file doesn't exist at that location")

    for line in f:
        print ("%s" %(line))

    f.seek(0, 0) # resetting the head to 0

    for line in f:
        print ("%s" %(line))

if __name__ == '__main__':
    print("Running Question One: ")
    queston_one()
    print("Running Question Two: ")
    question_two()