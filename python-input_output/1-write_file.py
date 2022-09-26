#!/usr/bin/python3
"""
Module write_file
"""


def number_of_lines(filename=""):
    """Returns the number of lines in a text file.
    Args:
        filename (str): name of file to be opened
    """
    with open(filename, mode="r", encoding='utf-8') as op:
        x = len(op.readline())
    return x
