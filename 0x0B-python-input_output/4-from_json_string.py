#!/usr/bin/python3
"""
This is the from_json_string module

The from_json_string module an object
(Python data structure) represented by a JSON string
"""


import json


def from_json_string(my_str):
    """Turns json str into python data struct"""
    return json.loads(my_str)
