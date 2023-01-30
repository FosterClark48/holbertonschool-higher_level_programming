#!/usr/bin/python3
"""
This is the class_to_json module

The class_to_json module returns the dictionary description
with simple data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object
"""


import json


def class_to_json(obj):
    """Returns dict representation"""
    return obj.__dict__
