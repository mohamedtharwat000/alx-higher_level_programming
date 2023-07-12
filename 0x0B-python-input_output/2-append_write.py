#!/usr/bin/python3

"""
    module for function append_write
"""


def append_write(filename="", text=""):
    """
        append_write - function that appends a string at the end of a text file
        (UTF8) and returns the number of characters added
        Args:
            filename (str): name of file
            text (str): text to append
        Return:
            int: the total number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
