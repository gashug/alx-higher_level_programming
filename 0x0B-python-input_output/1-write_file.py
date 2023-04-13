#!/usr/bin/python3
"""defines a txt file writing fn."""


def write_file(filename="", text=""):
    """writes a string to text file

    Args:
        filename (str): name of the file
        text (str): text to be written

    Returns:
    the number of characters written
    """
    with open(filename, "w") as file:
        file.write(text)

    return len(text)
