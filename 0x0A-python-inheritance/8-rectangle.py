#!/usr/bin/python3
"""
This is the Rectangle class

Rectangle class extends BaseGeometry class and 
raises an Error when required
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
