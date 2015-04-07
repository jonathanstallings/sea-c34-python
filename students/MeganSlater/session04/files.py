"""Do I have to close every file I open?"""


def open_file():
    import io
    f = io.open('secrets.txt', encoding='utf-8')
    secret_data = f.read
    print "Is this thing still running?"


"""Can I edit the file once I open it?  How?"""


def edit_file():
    f = io.open('secrets.txt', 'r+')
    f.write(u"I'm editing this file")
