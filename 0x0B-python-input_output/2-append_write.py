#!/usr/bin/python3
def append_write(filename="", text=""):
    """writes a string to text file
        returns the number of characters written
    """
    with open(filename, "a") as file:
        "open the file in append mode"
        file.write(text)

    return len(text)
