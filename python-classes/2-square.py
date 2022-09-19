#!/usr/bin/python3
"""More documentation."""


class Square:

    """
    Private
    instance attribute: size.
    """

    def __init__(self, size=0):
        """Instantiation with size."""
        if not isinstance(self, size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
