#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None) if key in a_dictionary else None
    return a_dictionary
