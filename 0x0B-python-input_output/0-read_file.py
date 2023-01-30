#!/usr/bin/python3
"""
This is the read_file module

The read_file module reads a txt file and prints it
"""


def read_file(filename=""):
    """Reads file and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
