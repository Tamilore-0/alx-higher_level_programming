#!/usr/bin/python3
"""
Module defines a Rectangle class that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class with attributes for width, height, x, y, and id.
    """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If width, height, x, or y is not an int.
            ValueError: If width, height, x, or y <= 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    # Getter and setter for width
    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        """Getter for the y attribute."""

        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        """Override the string representation of the Rectangle."""
        return (
            f"[Rectangle]\
 ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """
        function that assigns an argument to each attribute.
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        elif not args:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        return {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.height,
            'width': self.width,
        }
