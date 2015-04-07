import io


def read_outside_file_size():
    """What happens if I try read an improper part of file?"""
    foo = io.open('test.txt', encoding='utf-8')
    contents = foo.read(-4096)
    foo.close
    print(contents)


# read_outside_file_size()
# result: No error, and the file is read completely.


def read_without_encoding_set():
    """What if I don't set encoding?"""
    foo = io.open('test.txt')
    contents = foo.read()
    foo.close
    print(contents)


# read_without_encoding_set()
"""
result: File was read as normal on my system, but I know it is good
practice to specify encoding.
"""
