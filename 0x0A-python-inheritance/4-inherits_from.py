#!/usr/bin/python3
"""
This is the inherits_from Module

The inherits_from module returns True if the object is
an instance of a class that inherited (directly or indirectly)
from the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """Function that checks if obj is instance of subclass"""
    if type(obj) not in [a_class]:
        return (issubclass(type(obj), a_class))
    else:
        return False
