#!/usr/bin/python3
"""Module Base"""
import json


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Json string to file"""
        if list_objs:
            list_objs = [ele.to_dictionary() for ele in list_objs]
        with open(cls.__name__ + '.json'', 'w') as fp:
            fp.write(cls.to_json_string(list_objs))
