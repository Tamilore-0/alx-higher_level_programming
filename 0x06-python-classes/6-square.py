#!/usr/bin/python3
"""
Square module
"""


class Square:
    """
    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__(size=0, position=(0, 0)): Initializes a new Square instance.

        size: Property representing the size of the square.

        position: Property representing the position of the square.

        area(): Method to calculate the area of the square.

        my_print(): Method to print the square with a specified position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        a new instance
        Args:
        size (int): size of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        returns the coordinates of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the coordinates of the square
        """
        if (not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) or \
           value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print("")
            return
        else:
            if self.__position[1] > 0:
                for _ in range(self.__position[1]):
                    print()
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                print(self.__size * '#')
