#!/usr/bin/python3
"""
This is the lookup Module

The lookup module returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """Function that shows all attributes/methods of obj"""
    return (dir(obj))
