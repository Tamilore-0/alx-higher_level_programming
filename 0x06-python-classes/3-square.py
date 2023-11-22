#!/usr/bin/python3
"""
A module that defines a square class
"""


class Square:
    """
    Def
    """
    def __init__(self, size=0):
        """
        A new instance
        Args:
        size (int): size of the square (Default set to 0)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size * self.__size
