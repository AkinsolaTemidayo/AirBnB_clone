#!/usr/bn/python3
""" FileStorage that serializes instances to a JSON file and deserializes JSON file to instances """

import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """ serializes intances to JSON file and deserializes  JSON"""

    __file_path = "file.json" # Path to the JSON file (ex: file.json)
    __objects = {} # dictionary - store all objects by <class name>.id

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        '''create empty dictionary'''
        json_object = {}
        """ fill dictionary with elements __objects """
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        """ deserializes the JSON fle to __objects """
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                # jlo = json.load(f)
                for key, value in json.load(f).items():
                    attri_value = eval(value["__class_"])(**value)
                    self.__objects[key] = attri_value
        except FileNotFoundError:
            pass
