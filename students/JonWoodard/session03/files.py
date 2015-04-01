def file_read(quest1):
    """
    Define a question about reading files.
    Question 1:
        How do you read information from a file?
    """
    # insert code here
    import io
    f = io.open('secrets.txt', encoding='utf-8')
    secret_data = f.read()
    f.close()

    header_size = 4096
    f = open('secrets.txt')
    secret_header = f.read(header_size)
    secret_rest = f.read()
    f.close()

def file_write(quest2):
    """
    Define a question about writing files.
    Question 2:
        How do you write information to a file?
    """
    # insert code here
    outfile = io.open('output.txt', 'w')
    for i in range(10):
    outfile.write("this is line: %i\n"%i)
