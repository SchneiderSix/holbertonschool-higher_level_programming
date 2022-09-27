#!/usr/bin/python3
"""Module"""


def append_write(filename="", text=""):
    """Write file"""
    with open(filename, 'w+') as f:
        f.write(text)
        return text.count()
