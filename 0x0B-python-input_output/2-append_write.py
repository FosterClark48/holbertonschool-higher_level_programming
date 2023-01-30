#!/usr/bin/python3
"""
This is the append_write module

The append_write module appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """Appends a str to eof and returns len of char"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
