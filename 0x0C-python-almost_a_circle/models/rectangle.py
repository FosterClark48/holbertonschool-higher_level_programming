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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """returns value of attribute, width"""
        return self.width

    @width.setter
    def size(self, value):
        """sets value of attribute"""
        self.width = value

    @property
    def height(self):
        """returns value of attribute, height"""
        return self.height

    @height.setter
    def size(self, value):
        """sets value of attribute"""
        self.height = value

    @property
    def x(self):
        """returns value of attribute, x"""
        return self.x

    @x.setter
    def size(self, value):
        """Private setter for x"""
        self.x = value

    @property
    def y(self):
        """return value of attribute, y"""
        return self.y

    @y.setter
    def size(self, value):
        """sets value of attribute"""
        self.y = value
