#!/usr/bin/python3
""" More documentation. """


class Square:
    """
    Private
    instance attribute: size.
    """
    def __init__(self, size=0):
        """
        Instantiation with size.
        """
        self.__size = size

    @setter
    def size(self, value):
        """
        Set size to value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @retrieve_size
    def size(self):
        """
        Retrieve size.
        """
        return self.__size

    def area(self):
        """
        Return size squared.
        """
        return self.__size ** 2
