'''
This is for Task 8 - Files

The following are questions that I had when reading through the session04
lecture notes on reading and writing files.

1) Make a document. Read in the document. Then print every other line of the document.
2) Open and write to a new document
'''

# Question 1: Can I read in a document and print out every other line?

def read_and_print(file):
    f = open(file, 'r')
    for index, line in enumerate(f.readlines()):
        if index % 2 == 0:
            print line.strip()

# Question2: Can I open and write a new document where I print every letter of the 
# alphabet?

import string

def open_and_write(file):
    outfile = open(file, 'w')
    outfile.write("The letters of the alphabet backwards are: \n")
    for i in  list(string.ascii_lowercase)[::-1]:
        outfile.write(i+"\n")

if __name__ == "__main__":
    read_and_print("./files_test1.txt")

    open_and_write("./files_test2.txt")

'''
See files_test1.txt for original lyrics. Output once function is called:
    # These are lyrics from CHVRCHES's Recover. I like this song.
    And if I recover
    Or it can be over
    So pick any number
    I've got the answer
    I'll give you one more chance
    And you take what you need

See files_test2.txt for second function output. It worked!
'''
