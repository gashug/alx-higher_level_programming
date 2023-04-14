#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)

    for name in names:
        if name[:2] != '__':
            """checks the first 2 characters are not underscrores"""
            print(name)
