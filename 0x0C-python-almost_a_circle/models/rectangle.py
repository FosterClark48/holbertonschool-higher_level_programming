#!/usr/bin/python3
"""
This is the Rectangle class

Rectangle class extends Base class
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class extending Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Private initialization of class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Private getter for width"""
        return self.__width

    @width.setter
    def size(self, value):
        """Private setter for width"""
        self.__width = value

    @property
    def height(self):
        """Private getter for height"""
        return self.__height

    @height.setter
    def size(self, value):
        """Private setter for height"""
        self.__height = value

    @property
    def x(self):
        """Private getter for x"""
        return self.__x

    @x.setter
    def size(self, value):
        """Private setter for x"""
        self.__x = value

    @property
    def y(self):
        """Private getter for y"""
        return self.__y

    @y.setter
    def size(self, value):
        """Private setter for y"""
        self.__y = value
