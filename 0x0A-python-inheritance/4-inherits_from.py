#!/usr/bin/python3
"""
This is the inherits_from Module
"""


def inherits_from(obj, a_class):
    """Function that checks if obj is instance of subclass"""
    if type(obj) not in [a_class]:
        return (issubclass(type(obj), a_class))
    else:
        return False
