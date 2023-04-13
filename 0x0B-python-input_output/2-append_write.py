#!/usr/bin/python3
"""defines file appending fn"""


def append_write(filename="", text=""):
    """writes a string to text file

    Args:
        filename (str): name of the file to append to.
        text (str): string to append
    
    Returns:
        the number of characters written
    """
    with open(filename, "a") as file:
        "open the file in append mode"
        file.write(text)

    return len(text)
