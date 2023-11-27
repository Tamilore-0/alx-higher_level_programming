#!/usr/bin/python3
"""
Module with a Rectangle class for representing rectangles.
"""


class Rectangle:
    """
    Rectangle class for representing rectangles.

    Attributes:
    - __width (int): Width of the rectangle.
    - __height (int): Height of the rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with specified width and height.

        Args:
        - width (int): Width of the rectangle (default is 0).
        - height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
        int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
        int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calaculates and returns the area of the rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        calculates and returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += '#' * self.__width + '\n'
        return rectangle_str.rstrip()

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can recreate the object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor method for MyClass.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
