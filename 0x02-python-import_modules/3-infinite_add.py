#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_list = argv[1:]
    ctr = 0
    for i in range(len(arg_list)):
        ctr += int(arg_list[i])
    print(ctr)
