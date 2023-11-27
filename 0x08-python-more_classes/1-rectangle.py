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

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with specified width and height.

        Args:
        - width (int): Width of the rectangle (default is 0).
        - height (int): Height of the rectangle (default is 0).
        """
        self.__width = width
        self.__height = height
    
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
        """
        Set the width of the rectangle.

        Args:
        - value (int): New width value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than 0.
        """
        if type(self.__width) is not int:
           raise TypeError("width must be an integer")
        if self.__width < 0:
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
        """
        Set the height of the rectangle.

        Args:
        - value (int): New height value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than 0.
        """
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
