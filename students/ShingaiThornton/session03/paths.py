# Q1 How to display path using pathlib?


def displaypath():
    """
    Display current working directory path

    Args:

    Return: String containing current working directory path
    """

    import pathlib
    pth = pathlib.Path('./')
    pth.is_dir()
    pth.absolute()

displaypath()
