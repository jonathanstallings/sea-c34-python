# Paths (1 question)

# Question 1
import os


def read_a_file():
    """
    How do you view a list of all the files in a directory?
    Result:
        Prints files in that directory.
    """
    file_path = "~/Desktop"
    files_and_dirs = os.listdir(file_path)

    for files in files_and_dirs:
        print files
