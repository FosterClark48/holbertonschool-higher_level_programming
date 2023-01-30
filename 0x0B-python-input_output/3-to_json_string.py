#!/usr/bin/python3
"""
This is the to_json_string module

The to_json_string module returns the JSON
representation of an object (string)
"""


import json

def to_json_string(my_obj):
    """Turns python string into json dict"""
    return json.dumps(my_obj)
