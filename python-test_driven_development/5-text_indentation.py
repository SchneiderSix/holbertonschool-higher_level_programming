#!/usr/bin/python3
"""
Module text_indentation
"""


def text_indentation(text):
    """Print text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i])
            print()
            i += 1
        else:
            print(text[i], end='')
            i += 1
