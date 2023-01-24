#!/usr/bin/python3
""" This is the add_integer module """


def add_integer(a, b=98):
    """ Function to add 2 ints """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(round(a) + round(b))
