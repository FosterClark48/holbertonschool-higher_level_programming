#!/usr/bin/python3
"""
This is the Rectangle class
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
        """returns value of attribute, width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets value of attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns value of attribute, height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets value of attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns value of attribute, x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Private setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return value of attribute, y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets value of attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of Rectangle"""
        return self.width * self.height

    def display(self):
        """Prints rectangle using #s"""
        for colum in range(self.y):
            print()

        for i in range(self.__height):
            for row in range(self.x):
                print(" ", end="")

            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns str representation of Rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Assign an arg to each attribute"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        for key, val in kwargs.items():
            setattr(self, key, val)

    def to_dictionary(self):
        """Dict rep of a rect"""
        rect_dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return rect_dict
