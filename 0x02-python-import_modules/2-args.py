#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]  # skip the first argument, which is the script name
    num_args = len(args)

    if num_args == 0:
        print("No arguments.")
    else:
        print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")
        for i, arg in enumerate(args):
            print(f"{i+1}: {arg}")
