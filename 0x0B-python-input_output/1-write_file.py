#!/usr/bin/python3
def write_file(filename="", text=""):
    """writes a string to text file
        returns the number of characters written
    """
    with open(filename, "w") as file:
        file.write(text)

    return len(text)
