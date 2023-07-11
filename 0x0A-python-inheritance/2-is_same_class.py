#!/usr/bin/python3

"""
    module for the function is_same_class(obj, a_class).
"""


def is_same_class(obj, a_class):
    """
        is_same_class - function that returns True if the object is exactly
        an instance of the specified class ; otherwise False.
    Args:
        obj: object
        a_class: class
    Return:
        True or False.
    """
    return type(obj) is a_class
