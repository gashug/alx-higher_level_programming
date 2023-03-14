#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    num_args = len(args)

    if num_args == 0:
        print("No arguments.")
    elif num_args == 1:
        print("{} {}:".format(num_args, 'argument'))
        for i, arg in enumerate(args):
            print("{}: {}".format(i + 1, arg))
    else:
        print("{} {}:".format(num_args, 'arguments'))
        for i, arg in enumerate(args):
            print("{}: {}".format(i + 1, arg))
