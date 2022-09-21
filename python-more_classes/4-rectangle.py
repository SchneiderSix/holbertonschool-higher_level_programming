#!/usr/bin/python3
"""Module 3-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Retrieves an informal string representation of
        a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ''
        _print = ''
        for i in range(self.__height):
            for j in range(self.__width):
                _print += '#'
            _print += '\n'
        return _print[:-1]

    def __repr__(self):
        """Retrieves object representation of
        rectangle in string recreating new instance by using eval()"""
        return "Rectangle ({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        Args:
            value: value of the width, must be a positive integer
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        Args:
            value: value of the height, must be a positive integer
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retrieves area of a Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retrieves perimeter of a Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
