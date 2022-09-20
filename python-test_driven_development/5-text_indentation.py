#!/usr/bin/python3
"""
Module text_indentation
"""


def text_indentation(text):
    """Print text"""
    nice_text = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if i != '.' and i != '?' and i != ':':
            nice_text = nice_text + text[i]
        else:
            nice_text = nice_text + text[i]
            print(nice_text)
            print()
            print()
            nice_text = ""
    print(nice_text, end="")
