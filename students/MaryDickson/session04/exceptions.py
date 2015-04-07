# questions about the exceptions section in slides 4

list = [0, 1, 4, 8, 100, 1001]


def printitem(list, num):
    """
    Can I throw a warning message if number not in range?
    """
    try:
        return list[num]
    except:
        return(u"oops not long enough")
    finally:
        list.append(34)

print list
print printitem(list, 2)
print printitem(list, 10)
print list


def make_name_error(name):
    '''
    say hello given a name (string)
    '''
    try:
        print "Hello %s" % name
    except NameError:
        print "Oops, try that again with a string this time"
    finally:
        return "program finished"

print make_name_error(Mary)  # name error
print make_name_error("Mary")
