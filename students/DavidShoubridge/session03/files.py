def open_file():
    """Can I write a script that will open a file on my machine?
    """
    open("foo.txt", "wb")

open_file()  # Ended up creating a new file, but close.


def new_open():
    """ Can I add text to an already created file on my machine?
    """
    with open("foo.txt", "a") as file:
        file.write("Appended to!!!!!")

new_open()  # Not working yet.


def create_with_path():
    """ Can I create a new file using an absolute path?
    """