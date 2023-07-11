#!/usr/bin/python3

"""
    module for the function inherits_from(obj, a_class).
"""


def inherits_from(obj, a_class):
    """
        inherits_from - function that returns
        True if the object is an instance of a class that inherited directly or
        indirectly from the specified class,
        otherwise False.

        Args:
            obj: object
            a_class: class

        Return:
            True or False.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
