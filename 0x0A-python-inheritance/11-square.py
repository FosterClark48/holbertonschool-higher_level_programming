#!/usr/bin/python3
"""
This is the Square class

Square class extends Rectangle class and
raises an Error when required. It also implements
the area method and prints a formatted string
"""

# BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class extending BaseGeometry class"""
    def __init__(self, size):
        """initialization of class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """str method to print msg"""
        return "[Square] {}/{}".format(self.__size, self.__size)
