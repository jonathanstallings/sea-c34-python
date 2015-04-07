import pathlib


def iterdir():
    """What happen when you use iterdir on something
    that is not a directory?"""
    pth = pathlib.Path('./dictionaries.py')
    assert pth.is_dir() is False
    try:
        for f in pth.iterdir():
            print f
    except:
        print ("there's an issue using iterdir on non-directory")
# you cannot use iterdir on non-directory
