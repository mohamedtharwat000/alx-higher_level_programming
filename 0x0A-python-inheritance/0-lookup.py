#!/usr/bin/python3

"""
    module for the lookup(obj) function
"""

def lookup(obj):
    """
        lookup - function that takes an object as argument and returns
        a list of available attributes and methods of that object
        Args:
            obj: object to be looked up
        Returns:
            list: list of available attributes and methods of an object
    """
    return dir(obj)
