#!/usr/bin/python3
"""
Module rectangle
"""


class Rectangle:
    """Defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize private instance attributes"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return width"""
        return self.__width

    @property
    def height(self):
        """Return height"""
        return self.__height

    @widt_setter
    def width(self, value):
        """Set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height_setter
    def height(self, value):
        """Set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
