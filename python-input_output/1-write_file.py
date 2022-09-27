#!/usr/bin/python3
"""Module"""


def write_file(filename="", text=""):
    """Write file"""
    with open(filename, 'w') as f:
        return f.write(text)
