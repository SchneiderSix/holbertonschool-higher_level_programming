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
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the square with the character #."""
        if self.__size == 0:
            print()
            return None
        else:
            for i in range(0, self.__position[1]):
                print()
            for j in range(0, self.__size):
                for h in range(0, self.__position[0]):
                    print(" ", end="")
                for l in range(0, self.__size):
                    print("#", end="")
            print()


    @setter_position
    def position(self, value):
        """Sets the position to a value."""
        if len(value) != 2 or type(value) is not tuple \
        or type(value[0]) is not int or type(value[1]) is not int \
        or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
        
    @retrieve_position
    def position(self):
        """Retrieves the position."""
        return self.__position
