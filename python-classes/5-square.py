#!/usr/bin/python3
"""More documentation."""


class Square:

    """
    Private
    instance attribute: size.
    """

    def __init__(self, size=0):
        """Instantiation with size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    @setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @retrieve_size
    def size(self):
        return self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return None
        else:
            for i in range(1, self.area() + 1):
                print("#", end="")
