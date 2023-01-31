#!/usr/bin/python3
"""
This is the Base module
"""
import json


class Base:
    """Base class created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of instance for Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects