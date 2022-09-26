#!/usr/bin/python3
"""
Module write_file
"""


def append_write(filename="", text=""):
    """Put text into file
    a
    a
    a
    a
    a
    a
    a
    a
    a
    a
    a"""
    with open(filename, mode="w", encoding="utf-8") as wf:
        wf.write(text)
        return text.count()
