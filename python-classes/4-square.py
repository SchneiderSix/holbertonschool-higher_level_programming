#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        size (int): The size of the new square"""
        self.__size = size

    @property
    def size(self):
        """Get the size."""
        return self.__size

    @setter
    def size(self, value):
        """Sets size to value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns size squared."""
        return self.__size ** 2
