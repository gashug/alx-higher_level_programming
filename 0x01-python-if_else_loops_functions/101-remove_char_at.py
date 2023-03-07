#!/usr/bin/python3
def remove_char_at(str, n):
    if n in range(0, len(str) + 1):
        new_list = list(str)
        new_list.pop(n)

        new_string = ''.join(new_list)

        print(new_string)
    else:
        print(str)
