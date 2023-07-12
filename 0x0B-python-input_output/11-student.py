#!/usr/bin/python3

"""
    module for class Student
"""


class Student:
    """
        Student class
    """
    def __init__(self, first_name, last_name, age):
        """
            __init__ - constructor
            Args:
                first_name (str): first name
                last_name (str): last name
                age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(x) is str for x in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
            reload_from_json - reloads the instance attributes
            Args:
                json (dict): json to use
        """
        for k, v in json.items():
            self.__dict__[k] = v
