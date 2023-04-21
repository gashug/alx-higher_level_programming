#!/usr/bin/python3
"""defines the class Base"""
import json


class Base():
    """"empty class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base class with id

        Args:
            id (int)
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json rep of data"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json rep of data"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dictionary_list = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(dictionary_list)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            new_instance = None
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                list_dicts = cls.from_json_string(file.read())
                list_instances = [cls.create(**d) for d in list_dicts]
                return list_instances
        except FileNotFoundError:
            return []
