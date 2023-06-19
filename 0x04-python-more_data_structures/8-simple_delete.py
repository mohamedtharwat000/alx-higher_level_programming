#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # if key in a_dictionary: del a_dictionary[key]
    del a_dictionary[key] if key in a_dictionary else None
    return a_dictionary
