#!/usr/bin/python3
"""
This is the is_same_class Module

The is_same_class module returns True if the object is exactly an
instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """Function that checks if obj is instance of class"""
    return (type(obj) is a_class)
