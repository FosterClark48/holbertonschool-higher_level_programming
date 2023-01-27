#!/usr/bin/python3
"""
This is the is_kind_of_class Module

The is_kind_of_class module returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Function that checks if obj is instance of class or subclass"""
    return (isinstance(obj, a_class))
