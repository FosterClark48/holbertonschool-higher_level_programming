#!/usr/bin/python3
"""
This is the Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class extending Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns value of attribute, size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets value of attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns str representation of Rectangle"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Assign an arg to each attribute"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        for key, val in kwargs.items():
            setattr(self, key, val)

    def to_dictionary(self):
        """Dict rep of a square"""
        sq_dict = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return sq_dict
