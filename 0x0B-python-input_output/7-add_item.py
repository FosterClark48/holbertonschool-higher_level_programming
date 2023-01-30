#!/usr/bin/python3
"""
This is the add_item module

The add_item module adds all arguments
to a Python list, and then save them to a file
"""


import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

for arg in sys.argv[1:]:
    items.append(arg)

save_to_json_file(items, filename)
