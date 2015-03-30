# Q1 How to read and print a text file located on the web

def webtext():
    """
    Opens and prints text file located on the web

    Args:

    Returns: Content of text file
    """
    import urllib
    txt = urllib.urlopen("http://m.uploadedit.com/ba3b/1427242628701.txt").read()

    print txt

webtext()


# Q2 How does f.write work?

def fwritetest():
    """
    Write a string to a file then read the string

    Args:

    Returns: String from file
    """

    import StringIO

    s = StringIO.StringIO()
    s.write("This is a test")
    s.seek(0)
    s.read()

fwritetest()
