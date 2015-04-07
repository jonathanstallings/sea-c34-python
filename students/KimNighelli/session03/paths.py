import os

'''
This is for Task 8 - Paths

The following question came to me while reading the session04 lecture notes on files.

1) Can I print out every file in my directory using the OS module and defining some path?
'''

# Question 1: Can I print out every file in my directory using the OS module and defining some path?

def path_info(path):

    absolute_path = os.path.abspath(path)
    basename = os.path.basename(path)

    print "The absolute path to this file is %s" % (absolute_path)

    print "The basename of this program is %s" % (basename)

    # Print all the files in a set directory

    print "\nAll the current files in this directory are: "
    path = '.' #Current working directory
    for file in os.listdir(path):
        print file

    return absolute_path

if __name__ == "__main__":
    
    path_info('./paths.py')

'''
Output from the print statements:

The absolute path to this file is /Users/knighelli/Desktop/CodeFellows/sea-c34-python/students/KimNighelli/session03/paths.py
The basename of this program is paths.py

All the current files in this directory are:
    dictionaries.py
    exceptions.py
    files.py
    paths.py
'''
