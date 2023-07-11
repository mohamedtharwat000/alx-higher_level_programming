#!/usr/bin/python3

"""
    module for the function is_kind_of_class(obj, a_class).
"""


def is_kind_of_class(obj, a_class):
    """
        is_kind_of_class - function that returns
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class
        otherwise False.
        Args:
            obj: object
            a_class: class
        Returns: True or False.
    """
    if isinstance(obj, a_class):
        return True
    return False
