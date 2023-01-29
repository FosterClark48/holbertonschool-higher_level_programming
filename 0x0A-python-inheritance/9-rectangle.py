#!/usr/bin/python3
"""
This is the Rectangle class

Rectangle class extends BaseGeometry class and 
raises an Error when required. It also implements
the area method and prints a formatted string
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class extending BaseGeometry class"""
    def __init__(self, width, height):
        """initialization of class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area method returns area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """str method to print msg"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
