#!/usr/bin/python3

"""
    module for function read_file
"""


def read_file(filename=""):
    """
        read_file - that reads a text file (UTF8) and prints it to stdout.
        Args:
            filename (str): name of the file to be read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
