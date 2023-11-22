#!/usr/bin/python3
"""
Square module
"""


class Square:
    """
    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(size=0): Initializes a new Square instance.

        size: Property representing the size of the square.

        area(): Method to calculate the area of the square.

        my_print(): Method to print the square using '#' characters.
    """
    def __init__(self, size=0):
        """
        A new instance
        Args:
        size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        returns the size of the square
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

    def area(self):
        """
        calculates and returns the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(self.__size * '#')
