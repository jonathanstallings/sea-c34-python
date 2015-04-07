import pathlib


def set_nonexistant_path():
    """Can I set a non-existant path with pathlib?"""
    pth = pathlib.Path('./foo/')
    print(pth.is_dir())
    print(pth.absolute())


# set_nonexistant_path()
"""
result: Yes, I can set a nonexistant path, but pathlib knows
it is not a directory.
"""
