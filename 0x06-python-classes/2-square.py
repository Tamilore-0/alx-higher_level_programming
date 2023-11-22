#!/usr/bin/python3
"""
This module defines a square
"""


class Square:
    """
    Def
    """
    def __init__(self, size=0):
        """
        a new Square instance.
        Parameters:
        - size (int): The size of the square (default is 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
