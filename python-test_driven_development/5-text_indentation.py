#!/usr/bin/python3
"""
Module text_indentation
"""


def text_indentation(text):
    """Print text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    nt = ""
    while i < len(text):
        if text[i] not in ".:?":
            nt += text[i]
        else:
            nt += text[i]
            print(nt)
            print()
            nt = ""
            while i < (len(text) - 1) and text[i + 1] == " ":
                i += 1
        i += 1
    print(nt, end="")
