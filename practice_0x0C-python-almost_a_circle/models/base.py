#!/usr/bin/python3
import json
""" This module is the base of other classes"""
class Base:
    """ Represent the base model.
    Attributes:
        __nb_objects (int): the number of instanciated bases.
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
            a new base instanciated
            Args:
                id (int): the instnace identification
    `    """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding='utf-8') as myfile:
            if list_objs is None:
                myfile.write("[]")
            else:
                for item in list_objs:
                    list_dict = item.to_dictionary()
                    myfile.write(Base.to_json_string(list_dict))
    
    @staticmethod
    def from_json_string(json_string):
        if json_string == [] or json_string is None:
            return []
        else:
            return json.loads(json_string)

    def create(cls, **dictionary):
        __init__(width, height, x, y, id).Rectangle()
