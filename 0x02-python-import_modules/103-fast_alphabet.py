#!/usr/bin/python3
print(*(chr(i) for i in range(ord('A'), ord('Z')+1)), sep='')

import string

print(string.ascii_uppercase)
