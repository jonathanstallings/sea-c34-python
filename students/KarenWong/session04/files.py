import io


def read():
    """what is the difference between f.read() and f.readline()"""
    f = io.open("test.txt")
    line = f.read()
    print line
    f.close()
    f = io.open("test.txt")
    line = f.readline()
    print line
    f.close()
# f.read() read and printed the whole file, while f.readline only printed the
# first line of the file.


def readlines():
    """what is the difference between f.readline() and f.readlines()"""
    f = io.open("test.txt")
    line = f.readline()
    print line
    f.close()
    f = io.open("test.txt")
    line = f.readlines()
    print line
    f.close()
# f.readline printed the first line of the file, while f.readlines turned
# the lines of the file to an array of python objects.
