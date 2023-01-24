#!/usr/bin/python3
"""
This is the print_square module.

The print_square module takes in a string and prints it.
"""


def print_square(size):
    """ Function that prints first and last name """
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
