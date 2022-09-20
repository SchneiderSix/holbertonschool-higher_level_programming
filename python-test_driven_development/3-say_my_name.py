#!/usr/bin/python3
"""
Module say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Print name or msg error"""
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
