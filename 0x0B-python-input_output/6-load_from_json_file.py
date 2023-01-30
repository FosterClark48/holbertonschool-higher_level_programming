#!/usr/bin/python3
"""
This is the save_to_json_file module

The save_to_json_file module that writes an
Object to a text file, using a JSON representation
"""


import json


def load_from_json_file(filename):
    """Creates obj from json file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
