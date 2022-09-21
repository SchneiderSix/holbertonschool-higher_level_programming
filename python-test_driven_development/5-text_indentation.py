#!/usr/bin/python3
"""
Module text_indentation
"""


def text_indentation(text):
    """Print text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    flag = 0
    while i < len(text):
        if text[i] not in ".:?":
            print(text[i], end="")
            flag = 1
        else:
            if text[i] == '.':
                print(".", end="")

            if text[i] == '?':
                print("?", end="")

            if text[i] == ':':
                print(":", end="")

            if flag == 1:
                i += 1
                print(text[i].strip())
            flag = 0
            print(text[i])
        i += 1
