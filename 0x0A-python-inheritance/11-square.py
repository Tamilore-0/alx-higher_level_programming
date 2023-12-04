#!/usr/bin/python3
"""
Square Module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that inherits from the rectangle class
    """

    def __init__(self, size):
        """
        ...
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        calculates and returns area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: The Square description.
        """
        return f"[Square] {self.__size}/{self.__size}"
