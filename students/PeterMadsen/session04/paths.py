import os

def question_one():
    """How would I find a module that is a cousin of this module?

        For instance how could I open up list_lab.py in the session03 dir?
    """
cur_dir = os.getcwd()

path_to_module = os.path.relpath("../session03/list_lab.py", cur_dir)

print (os.path.isfile(path_to_module))

#*********************** TEST CODE *********************** #
if __name__ == '__main__':
    question_one()