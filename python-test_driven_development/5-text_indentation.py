#!/usr/bin/python3
"""
Module text_indentation
"""


def text_indentation(text):
    """Print text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    c = 0
    while c < len(text):
        if text[c] in ['.', '?', ':']:
            print(text[c])
            print()
            c += 1
        else:
            print(text[c], end='')
        c += 1
