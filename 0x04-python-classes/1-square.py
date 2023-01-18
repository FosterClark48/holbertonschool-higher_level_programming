#!/usr/bin/python3
"""Square class that defines a square"""


class Square:
    """Passing initializing values to object"""
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
