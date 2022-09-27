#!/usr/bin/python3
"""Module"""


def append_write(filename="", text=""):
    """Write file"""
    if text:
        if not filename:
            with open(filename, 'w+') as f:
                f.write(text)
        else:
            with open(filename, 'w') as f:
                f.write(text)
        return len(text)
