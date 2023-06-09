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
        """
            to_json - retrieves a dictionary representation of a Student instance
            Args:
                attrs (list): list of attributes
            Returns:
                dictionary
        """
        if type(attrs) is list and all(type(x) is str for x in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
