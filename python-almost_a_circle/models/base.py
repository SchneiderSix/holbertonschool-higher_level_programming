#!/usr/bin/python3
"""Module Base"""


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor
        id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects