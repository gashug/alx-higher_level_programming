#!/usr/bin/python3
"""defines json file writing fn."""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to text file using JSON rep"""
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
