#!/usr/bin/python3
"""
Module write_file
"""


def number_of_lines(filename=""):
    """Return the num of lines in a file.
    Args:
        filename (str): name of file to be opened
    """
    with open(filename, encoding='utf-8') as op:
        x = len(op.readline())
    return x
