#!/usr/bin/python3
"""
This is the add_integer module.

This module supplies one function, add_integer(),
which adds together 2 int or float types and returns an int.
"""


def add_integer(a, b=98):
    """Function to add 2 ints"""
    
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
