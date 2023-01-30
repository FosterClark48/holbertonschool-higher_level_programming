#!/usr/bin/python3
"""
This is the write_file module

The write_file module writes a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Reads file and prints to stdout"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
