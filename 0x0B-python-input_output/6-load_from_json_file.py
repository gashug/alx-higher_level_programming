#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """creates an object from a JSON file"""
    with open(filename, "r") as file:
        """open file in read mode"""
        return json.loads(file.read())
