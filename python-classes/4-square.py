#!/usr/bin/python3
"""Class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        size (int): The size of the new square"""
        self.__size = size

    @getter
    def size(self):
        """Get size of the square."""
        return self.__size

    @setter
    def size(self, value):
        """Set the size to value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return size squared"""
        return self.__size ** 2
