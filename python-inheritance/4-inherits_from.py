#!/usr/bin/python3
"""
Module is_kind_of_class
"""


def inherits_from(obj, a_class):
    """Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
    a
    a
    a
    a
    """
    return isinstance(obj, a_class) and type(obj) is not a_class 
