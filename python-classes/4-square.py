#!/usr/bin/python3

"""Module, class Square
.
.
.
"""


class Square:

    """Private attribute: size
    .
    .
    .
    """

    def __init__(self, size=0):

        """Instantiation with size
        .
        .
        .
        """

        self.__size = size

    @setter
    def size(self, value):

        """Set value for size
        .
        .
        .
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @retrieve_size
    def size(self):

        """Retrieve size
        .
        .
        .
        """

        return self.__size

    def area(self):

        """Return size squared
        .
        .
        .
        """

        return self.__size ** 2
