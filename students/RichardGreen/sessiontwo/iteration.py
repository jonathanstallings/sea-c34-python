'''Lets make a sequence of numbers to iterate through.
   Next lets make a string of characters'''

nums = range(25)

s = 'a b c d e f g h i j k l m n o p'


def print_second_num(s):
    '''print the second value of each letter in the sequence and double it'''
    i = 0
    if i < len(s):
        print 2 * (s[i])
    i = i + 2


def add_numbers(n):
    '''use iteration to add the sequence together'''
    sum = 0
    for item in n:
        sum += item
    print sum


def looking_for_abc(s):
    '''Lets iterate through our sequence until we reach a user defined character.
    if we dont find it exit'''
    items = ''
    letters = s.split()
    for items in letters:
        if items == 'a':
            print "TRUE"

        if items == 'b':
            print "TRUE"

        else:
            print "FALSE"

if __name__ == '__main__':
    print_second_num(s)
    add_numbers(nums)
    looking_for_abc(s)
