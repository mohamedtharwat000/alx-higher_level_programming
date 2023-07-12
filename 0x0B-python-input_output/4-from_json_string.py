#!/usr/bin/python3

"""
    module for function from_json_string
"""
import json


def from_json_string(my_str):
    """
        from_json_string - function that returns an object (Python data
        structure) represented by a JSON string.
        Args:
            my_str (str): JSON string
        Return:
            Python data structure
    """
    return json.loads(my_str)
