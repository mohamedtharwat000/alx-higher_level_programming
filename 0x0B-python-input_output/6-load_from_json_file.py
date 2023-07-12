#!/usr/bin/python3

"""
    module for function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
        load_from_json_file - function that creates an Object from “JSON file”
        Args:
            filename: name of file
        Return:
            object
    """
    with open(filename, 'r') as file:
        return json.load(file)
