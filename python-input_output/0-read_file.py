#!/usr/bin/python3
"""
Module read_file
"""


def read_file(filename=""):
    with open(filename, mode="r") as rf:
        print(rf.read())
