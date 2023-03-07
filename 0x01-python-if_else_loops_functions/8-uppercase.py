#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            new_string = new_string + chr(ord(i) - 32)
        else:
            new_string = new_string + i

    print(new_string)
