#!/usr/bin/python3
"""Class Square."""


class Square:
    """Square
    Attributes:
        __size (int): size of square's side
    """

    def __init__(self, size=0):
        """initializes the square
        Args:
            ssiz (int): size of square's side
        Returns:
            None
        """
        self.__size = size

    def area(self):
        """Size squared
        Returns:
            The area of the square
        """
        return self.__size ** 2

    @setter
    def size(self, value):
        """Setter
        Args:
            value (int): size of square's side
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @retrieve_size
    def size(self):
        """Getter
        Returns: Size
        """
        return self.__size
