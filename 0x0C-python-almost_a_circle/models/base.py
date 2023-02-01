#!/usr/bin/python3
"""
This is the Base module
"""
import json


class Base:
    """Base class created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of instance for Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json str rep"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes json str rep of obj to file"""
        filename = cls.__name__ + ".json"
        dict_list = []
        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dict_list))

    def from_json_string(json_string):
        """returns list of json str rep"""
        if json_string is None or json_string == 0:
            return ([])
        return json.loads(json_string)
