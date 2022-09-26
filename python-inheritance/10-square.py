#!/usr/bin/python3
"""
Module Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is a class
    s
    s
    s
    """
    def __init__(self, size:
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
