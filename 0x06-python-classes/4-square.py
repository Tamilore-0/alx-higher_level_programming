#!/usr/bin/python3
"""
Square module
"""


class Square:
    """
    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(size=0): Constructor method.
            Initializes a new Square instance.

        area(): Method to calculate the area of the square.

    Properties:
        size (int): Property representing the size of the square.
            Can be accessed and modified using the size property.
    """
    def __init__(self, size=0):
        """
        Constructor method
        Args:
        size (int): size of the square
        """
        self.__size = size

    def area(self):
        """
        Calculate and returns area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        returns size ofthe square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
