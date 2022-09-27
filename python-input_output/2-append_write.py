#!/usr/bin/python3
"""Module"""


def append_write(filename="", text=""):
    """append and return numb of chars added"""
    with open(filename, 'a+') as f:
        return f.write(text)
