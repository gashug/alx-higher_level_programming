#!/usr/bin/python3
"""adds aall args to a list and saves them in a file"""

from sys import argv

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

for arg in argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")
