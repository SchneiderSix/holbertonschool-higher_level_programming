#!/usr/bin/python3
"""
Module read_file
"""


def read_file(filename=""):
    """Print content of file"""
    with open(filename, mode="r", encoding="utf-8") as rf:
        print(rf.read(), end="")
