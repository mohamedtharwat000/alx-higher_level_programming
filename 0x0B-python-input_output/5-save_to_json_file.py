#!/usr/bin/python3

"""
    module for function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
        save_to_json_file - function that writes an Object to a text file,
        using a JSON representation.
        Args:
            my_obj: object to write
            filename: name of the file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
