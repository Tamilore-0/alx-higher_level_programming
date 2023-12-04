#!/usr/bin/python3
"""
Modules defines an BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class.
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        """
        Raises an exception
        indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
    