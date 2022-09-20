#!/usr/bin/python3
"""
Module print_square
"""


def print_square(size):
    """Print a square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    print('\n'.join([''.join('#' * size)] * size))
