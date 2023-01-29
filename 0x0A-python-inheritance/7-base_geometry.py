#!/usr/bin/python3
"""
This is the BaseGeometry class
"""


class BaseGeometry:
    """ declaring empty class """
    pass

    def area(self):
        """ Area method to raise Exception """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Int validator method to check for ints """
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
