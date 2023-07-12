#!/usr/bin/python3

"""
    module for function to_json_string
"""
import json


def to_json_string(my_obj):
    """
        to_json_string - function that returns the JSON representation of an
        object (string).
        Args:
            my_obj: object to be converted
        Returns:
            str: JSON representation of an object
    """
    return json.dumps(my_obj)
