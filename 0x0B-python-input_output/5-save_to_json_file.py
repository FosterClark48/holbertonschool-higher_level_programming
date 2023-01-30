#!/usr/bin/python3
"""
This is the save_to_json_file module

The save_to_json_file module that writes an
Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes obj to txt file using json representation"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
