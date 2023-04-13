#!/usr/bin/python3
"""defines a txt file rdng function"""


def read_file(filename=""):
    """function that reads text file"""
    with open(filename, "r") as file:
        print(file.read(), end="")
