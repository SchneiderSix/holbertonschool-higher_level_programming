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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static Method json of dict rep"""
        if not list_dictionaries:
            return []
        return str(json.dumps(list_dictionaries))
