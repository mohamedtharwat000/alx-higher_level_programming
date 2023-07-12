#!/usr/bin/python3

"""
    module for function write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """
        write_file - function that writes a string to a text file (UTF8)
        and returns the number of characters written.
        Args:
            filename (str): name of file to write to.
            text (str): text to write to file.
        Returns:
            number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
