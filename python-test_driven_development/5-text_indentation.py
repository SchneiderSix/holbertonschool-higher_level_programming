#!/usr/bin/python3
"""
Module text_indentation
"""


def text_indentation(text):
    """Print text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    cpy = text
    i = 0
    flag = 0
    while i < len(text):
        if text[i] not in ".:?":
            print(text[i], end="")
            flag = 1
        else:
            if text[i] == '.':
                print(".", end="")
                i += 1
            if text[i] == '?':
                print("?", end="")
                i += 1
            if text[i] == ':':
                print(":", end="")
                i += 1
            if flag == 1:
                i += 1
                print(text[i])
            flag = 0
            print(text[i])
        i += 1
